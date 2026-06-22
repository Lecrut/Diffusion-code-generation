def is_word_long(word):
    length_threshold = 10
    return len(word) > length_threshold

if __name__ == '__main__':
    sample_words = [
        "short",
        "thisisalongstring",
        "onlyletters",
        "this has a space",
        "abcdefghij",
        "a" * 11,
        "1234567890"
    ]
    for word in sample_words:
        result = is_word_long(word)
        print(f"Input: '{word}', Result: {result}")