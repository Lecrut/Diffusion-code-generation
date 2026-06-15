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
    file_contents