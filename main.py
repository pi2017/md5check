'''
MD5 checksum checker for large file
22.07.2020
Author: Savchenko O.V.
Company Makerobot
'''
import hashlib
import pathlib

filename = input("Enter the file name: ")
file = pathlib.Path(filename)
if file.exists():
    md5_hash = hashlib.md5()
    with open(file, "rb") as f:
    # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
            print('MD5 checksum: ', md5_hash.hexdigest())
else:
    print("File not exist")