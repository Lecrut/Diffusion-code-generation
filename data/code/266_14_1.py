def count_words(file_path):
    with open(file_path, 'r') as file:
        return sum(len(line.split()) for line in file)

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines.\nEach line has words."
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    
    print(count_words('sample.txt'))