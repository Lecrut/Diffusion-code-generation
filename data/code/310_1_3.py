import os
def print_two_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as f1:
            print(f1.read())
        with open(file2_path, 'r') as f2:
            print(f2.read())
    except FileNotFoundError as e:
        print(f"Error: One of the files was not found. Details: {e}")
if __name__ == '__main__':
    with open("file1.txt", "w") as f:
        f.write("This is the content of the first file.\n")
    with open("file2.txt", "w") as f:
        f.write("This is the content of the second file.\n")
    print_two_files("file1.txt", "file2.txt")
    print_two_files("file1.txt", "nonexistent.txt")