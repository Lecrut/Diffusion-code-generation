def file_exists(file_path):
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False

def word_generator(file_path):
    if not file_exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word.lower()

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    for word in word_generator(sample_file_path):
        print(word)