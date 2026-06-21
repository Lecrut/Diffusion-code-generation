def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word

if __name__ == '__main__':
    generator = word_generator('sample.txt')
    print(next(generator))
    print(next(generator))