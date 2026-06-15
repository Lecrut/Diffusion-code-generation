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
    sample_files = ["test_file_a.txt", "test_file_b.txt"]
    with open(sample_files[0], 'w') as f:
        f.write("This is the content of file A.")
    with open(sample_files[1], 'w') as f:
        f.write("This is the content of file B.")
    file_paths = sample_files + ["nonexistent_file.txt"]
    file_contents = []
    for path in file_paths:
        try:
            with open(path, 'r') as f:
                content = f.read()
                file_contents.append(content)
        except FileNotFoundError:
            file_contents.append(f"Error: File not found at {path}")
    print(file_contents)