import os
FILE_PATH = 'sample.txt'

def word_generator(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word.lower()
if __name__ == '__main__':
    try:
        for word in word_generator(FILE_PATH):
            print(word)
    except FileNotFoundError as e:
        print(e)