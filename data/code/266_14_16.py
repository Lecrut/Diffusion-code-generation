def count_words(file_path):
    with open(file_path, 'r') as file:
        return sum(len(line.split()) for line in file)

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines.\nEach line has words."
    temp_file_path = 'sample.txt'
    with open(temp_file_path, 'w') as file:
        file.write(sample_text)
    
    word_count = count_words(temp_file_path)
    print(word_count)