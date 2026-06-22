def count_words(file_path):
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines and words."
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    
    print(count_words('sample.txt'))