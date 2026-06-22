def count_words(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file for word in line.split())

if __name__ == '__main__':
    print(count_words('sample.txt'))