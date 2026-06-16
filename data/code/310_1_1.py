import os
def print_two_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as f1:
            print(f1.read())
        with open(file2_path, 'r') as f2:
            print(f2.read())
    except FileNotFoundError as e:
        print(f"Error: One of the files was not found - {e}")
if __name__ == '__main__':
    file1 = "file1.txt"
    file2 = "file2.txt"
    with open(file1, 'w') as f:
        f.write("This is the content of the first file.\n")
    with open(file2, 'w') as f:
        f.write("This is the content of the second file.\n")
    print_two_files(file1, file2)
    file3 = "nonexistent.txt"
    print_two_files(file1, file3)