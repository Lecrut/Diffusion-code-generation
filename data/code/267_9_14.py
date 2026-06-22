def is_word_long(word):
    min_length = 10
    return len(word) > min_length

if __name__ == '__main__':
    test_words = [
        "short",
        "thisisalongstring",
        "onlyletters",
        "this has a space",
        "abcdefghij",
        "a" * 11,
        "1234567890"
    ]
    for word in test_words:
        result = is_word_long(word)
        print(f"Input: '{word}', Result: {result}")