def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_file_path = "sample.txt"
    word_count = count_words(sample_file_path)
    print(word_count)