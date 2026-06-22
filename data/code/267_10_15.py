def is_word_long(word):
    return len(word) > 5

if __name__ == '__main__':
    test_words = {
        "short": False,
        "longerword": True,
        "example": True,
        "hi": False,
        "Python": True
    }
    
    for word, expected in test_words.items():
        result = is_word_long(word)
        print(f"Is '{word}' long? {result} (Expected: {expected})")