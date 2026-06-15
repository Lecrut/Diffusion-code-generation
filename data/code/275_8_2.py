import os
def filter_txt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print(filename)
if __name__ == '__main__':
    sample_directory = "."
    filter_txt_files(sample_directory)