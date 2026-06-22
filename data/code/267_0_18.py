def is_long(word):
    return len(word) > 10

if __name__ == '__main__':
    sample_word_one = "short"
    sample_word_two = "thisisalongword"
    sample_word_three = "tenchars"
    result_one = is_long(sample_word_one)
    print(f"'{sample_word_one}' is long: {result_one}")
    result_two = is_long(sample_word_two)
    print(f"'{sample_word_two}' is long: {result_two}")
    result_three = is_long(sample_word_three)
    print(f"'{sample_word_three}' is long: {result_three}")