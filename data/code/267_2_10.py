def is_word_long(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return len(text) > 20

if __name__ == '__main__':
    sample1 = "This is a short sentence"
    sample2 = "This is a very long sentence that definitely exceeds twenty characters"
    sample3 = "Exactly twenty characters"
    print(f"'{sample1}' is long: {is_word_long(sample1)}")
    print(f"'{sample2}' is long: {is_word_long(sample2)}")
    print(f"'{sample3}' is long: {is_word_long(sample3)}")