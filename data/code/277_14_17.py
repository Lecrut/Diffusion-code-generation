def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    word_count = count_words(sample_text)
    print(word_count)