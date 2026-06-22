def count_words(file_path):
    WORD_DELIMITERS = ' \t\n\r\f\v'
    
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = [word.strip(WORD_DELIMITERS) for word in line.split()]
            word_count += len(words)
    return word_count

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines and words."
    temp_file_path = 'sample.txt'
    with open(temp_file_path, 'w') as file:
        file.write(sample_text)
    result = count_words(temp_file_path)
    print(result)