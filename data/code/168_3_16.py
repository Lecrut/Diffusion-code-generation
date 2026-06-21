import os.path

def group_files_by_extension(file_paths):
    if not all(isinstance(path, str) for path in file_paths):
        raise ValueError("All items in file_paths must be strings")

    grouped_files = {}
    
    for path in file_paths:
        _, ext = os.path.splitext(path)
        ext = ext.lower()
        
        if ext not in grouped_files:
            grouped_files[ext] = []
            
        grouped_files[ext].append(path)
    
    return grouped_files

if __name__ == '__main__':
    sample_list = [
        "file1.txt",
        "image1.png",
        "document1.pdf",
        "file2.txt",
        "image2.jpg"
    ]
    print(group_files_by_extension(sample_list))