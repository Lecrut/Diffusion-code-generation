import os
import itertools
def synchronized_alternating_read(file1_path, file2_path):
    with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
        while True:
            chunk1 = f1.read(4096)
            chunk2 = f2.read(4096)
            if not chunk1 and not chunk2:
                break
            if chunk1:
                print(chunk1.decode('utf-8', errors='ignore'), end='')
            if chunk2:
                print(chunk2.decode('utf-8', errors='ignore'), end='')
if __name__ == '__main__':
    file1_name = "large_file1.txt"
    file2_name = "large_file2.txt"
    with open(file1_name, 'w') as f:
        f.write("This is the content of the first large file.\n" * 50000)
    with open(file2_name, 'w') as f:
        f.write("This is the content of the second large file.\n" * 50000)
    synchronized_alternating_read(file1_name, file2_name)