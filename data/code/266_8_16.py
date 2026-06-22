def count_words_in_string(text):
    word_count = len(text.split())
    return word_count

if __name__ == '__main__':
    sample_text = "This is a sample text for counting words, including punctuation and casing."
    print(count_words_in_string(sample_text))