def check_filenames(filenames):
    for filename in filenames:
        if filename.endswith('.txt'):
            print(filename)
if __name__ == '__main__':
    sample_files = [
        "document1.txt",
        "image.jpg",
        "report.txt",
        "data.csv",
        "notes.txt"
    ]
    check_filenames(sample_files)