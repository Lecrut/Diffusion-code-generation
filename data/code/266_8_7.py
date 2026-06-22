def count_words_in_string(text):
    words = text.lower().split()
    return len(words)

if __name__ == '__main__':
    sample_text = "This is a Sample Text for Testing the Word Count Function. It Contains Several Words and Punctuation Marks."
    word_count = count_words_in_string(sample_text)
    print(word_count)