def count_words_in_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        return -1
if __name__ == '__main__':
    sample_file_content = "This is a sample text file for testing the word count utility. It contains several words and some punctuation."
    sample_filename = "sample_text.txt"
    with open(sample_filename, 'w') as f:
        f.write(sample_file_content)
    word_count = count_words_in_file(sample_filename)
    print(word_count)