def is_word_long(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return len(word) > 10

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
        try:
            result = is_word_long(word)
            print(f"Input: '{word}', Result: {result}")
        except ValueError as e:
            print(e)