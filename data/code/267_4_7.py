LONG_WORD_THRESHOLD = 10

def is_word_long(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    for word in sample_words:
        print(f"The word '{word}' is long: {is_word_long(word)}")