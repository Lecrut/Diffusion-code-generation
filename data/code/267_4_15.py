WORD_LENGTH_THRESHOLD = 10

def is_word_long(word):
    return len(word) > WORD_LENGTH_THRESHOLD

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    for word in sample_words:
        print(f"The word '{word}' is long: {is_word_long(word)}")