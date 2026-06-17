def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        return -1
if __name__ == '__main__':
    sample_filename = "sample.txt"
    sample_content = "This is a sample text file for testing the word count utility."
    with open(sample_filename, 'w') as f:
        f.write(sample_content)
    word_count = count_words_in_file(sample_filename)
    print(word_count)