def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word.lower()

if __name__ == '__main__':
    sample_file_path = 'example.txt'
    for word in word_generator(sample_file_path):
        print(word)