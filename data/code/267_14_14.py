def any_word_exceeds_7_chars(words):
    for word in words:
        if len(word) > 7:
            return True
    return False

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(any_word_exceeds_7_chars(sample_words))