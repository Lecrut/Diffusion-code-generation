def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    word_gen = word_generator(sample_file_path)
    print(next(word_gen))
    print(next(word_gen))