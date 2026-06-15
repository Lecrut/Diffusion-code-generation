import os
def filter_txt_files(directory):
    filenames = os.listdir(directory)
    for filename in filenames:
        if filename.endswith(".txt"):
            print(filename)
if __name__ == '__main__':
    sample_directory = "."
    filter_txt_files(sample_directory)