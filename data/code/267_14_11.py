MAX_WORD_LENGTH = 7

def has_long_word(words):
    for word in words:
        if len(word) > MAX_WORD_LENGTH:
            return True
    return False

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(has_long_word(sample_words))