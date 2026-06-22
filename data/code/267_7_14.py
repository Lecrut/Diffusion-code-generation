LONG_WORD_THRESHOLD = 10

def is_long_word(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    sample_words = ["apple", "pineapple"]
    for word in sample_words:
        print(f"Word: {word}, Is Long: {is_long_word(word)}")