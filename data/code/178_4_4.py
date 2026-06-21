def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

if __name__ == '__main__':
    gen = word_generator('sample.txt')
    print(next(gen))
    print(next(gen))