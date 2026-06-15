import os
file_paths = ["file1.txt", "file2.txt", "nonexistent.txt"]
file_contents = []
for path in file_paths:
    try:
        with open(path, 'r') as f:
            content = f.read()
            file_contents.append(content)
    except FileNotFoundError:
        file_contents.append(f"Error: File not found at {path}")
if __name__ == '__main__':
    file_contents = []
    sample_files = ["test_file1.txt", "test_file2.txt"]
    with open(sample_files[0], 'w') as f:
        f.write("This is the content of file one.")
    with open(sample_files[1], 'w') as f:
        f.write("This is the content of file two.")
    file_paths = [sample_files[0], sample_files[1], "nonexistent.txt"]
    file_contents = []
    for path in file_paths:
        try:
            with open(path, 'r') as f:
                content = f.read()
                file_contents.append(content)
        except FileNotFoundError:
            file_contents.append(f"Error: File not found at {path}")
    print(file_contents)