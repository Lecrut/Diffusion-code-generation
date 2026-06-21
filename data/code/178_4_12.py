def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word.lower()

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    word_iter = word_generator(sample_file_path)
    for _ in range(5):
        print(next(word_iter))