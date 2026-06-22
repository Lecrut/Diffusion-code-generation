def is_valid_word(word):
    if not isinstance(word, str) or not word.isalpha():
        raise ValueError("Input must be a non-empty alphabetic string")

def is_long_word(word):
    is_valid_word(word)
    return len(word) > 10

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
        try:
            print(f"Input: '{word}', Result: {is_long_word(word)}")
        except ValueError as e:
            print(e)