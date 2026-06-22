def is_long_word(word):
    min_length = 10
    return len(word) > min_length

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    for word in sample_words:
        print(f"The word '{word}' is long: {is_long_word(word)}")