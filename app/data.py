import os
import hashlib
import zlib

GIT_DIR = '.mini-git'


def init():
    # Instead of creating .git repo I created .mini-git repo so it doesn't clash with the actual .git repo
    os.mkdir(GIT_DIR)
    os.mkdir(f"{GIT_DIR}/objects")
    os.mkdir(f"{GIT_DIR}/refs")
    with open(f"{GIT_DIR}/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")


def hash_object(file_content):
    file_hash = hashlib.sha1(file_content).hexdigest()
    os.mkdir(f"{GIT_DIR}/objects/{file_hash[:2]}")
    with open(f"{GIT_DIR}/objects/{file_hash[:2]}/{file_hash[2:]}", "wb") as f:
        f.write(zlib.compress(file_content))
    return file_hash


def cat_file(file_hash):
    file_path = f"{GIT_DIR}/objects/{file_hash[:2]}/{file_hash[2:]}"
    with open(file_path, "rb") as f:
        raw_data = zlib.decompress(f.read())
        return raw_data.decode("utf-8")
