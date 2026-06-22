def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text = "This is an example of a test string"
    word_count = count_words(sample_text)
    print(word_count)