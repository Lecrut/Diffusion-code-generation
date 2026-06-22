def any_word_exceeds_7_chars(words):
    return any(len(word) > 7 for word in words)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(any_word_exceeds_7_chars(sample_words))