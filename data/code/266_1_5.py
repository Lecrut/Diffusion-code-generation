def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

if __name__ == '__main__':
    print(count_words('sample.txt'))