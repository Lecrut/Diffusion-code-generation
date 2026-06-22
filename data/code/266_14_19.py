def count_words(filename):
    with open(filename, 'r') as file:
        return sum(len(line.split()) for line in file)

if __name__ == '__main__':
    print(count_words('sample.txt'))