import os

def group_by_extension(file_paths):
    if not all(isinstance(path, str) and os.path.exists(path) for path in file_paths):
        raise ValueError("All paths must be valid strings")
    
    grouped_files = {}
    for path in file_paths:
        _, ext = os.path.splitext(path)
        ext = ext.lower()
        if ext not in grouped_files:
            grouped_files[ext] = []
        grouped_files[ext].append(path)
    
    return grouped_files

if __name__ == '__main__':
    sample_paths = [
        "document.txt",
        "image.png",
        "report.pdf",
        "script.py",
        "archive.zip"
    ]
    print(group_by_extension(sample_paths))