def is_long_word(word, max_length=10):
    return len(word) > max_length

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    for word in sample_words:
        print(f"Is '{word}' a long word? {is_long_word(word)}")