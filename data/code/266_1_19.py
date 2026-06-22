def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    word_count = count_words(sample_file_path)
    print(f'The total number of words in "{sample_file_path}" is: {word_count}')