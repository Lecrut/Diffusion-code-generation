def is_long(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return len(word) > 10

if __name__ == '__main__':
    sample_word_one = "short"
    sample_word_two = "thisisalongword"
    sample_word_three = "tenchars"

    print(f"'{sample_word_one}' is long: {is_long(sample_word_one)}")
    print(f"'{sample_word_two}' is long: {is_long(sample_word_two)}")
    print(f"'{sample_word_three}' is long: {is_long(sample_word_three)}")