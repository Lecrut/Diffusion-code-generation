MIN_WORD_LENGTH = 8

def is_word_long(word):
    return len(word) > MIN_WORD_LENGTH

if __name__ == '__main__':
    test_words = [
        "short",
        "thisisalongstring",
        "onlyletters",
        "this has a space",
        "abcdefghij",
        "a" * 12,
        "1234567890"
    ]
    for word in test_words:
        print(f"Input: '{word}', Result: {is_word_long(word)}")