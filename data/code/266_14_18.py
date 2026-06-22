def count_words(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file for word in line.split())

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines and words."
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    
    print(count_words('sample.txt'))