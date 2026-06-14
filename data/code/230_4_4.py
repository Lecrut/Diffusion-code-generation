def check_txt_files(filenames):
    for filename in filenames:
        if filename.endswith('.txt'):
            print(filename)
if __name__ == '__main__':
    sample_filenames = [
        "document1.txt",
        "image.jpg",
        "report.txt",
        "data.csv",
        "notes.txt",
        "config.ini"
    ]
    check_txt_files(sample_filenames)