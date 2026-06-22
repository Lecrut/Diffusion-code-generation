MAX_LENGTH = 10

def is_long(word):
    return len(word) > MAX_LENGTH

if __name__ == '__main__':
    sample_word_one = "short"
    sample_word_two = "thisisalongword"
    print(f"'{sample_word_one}' is long: {is_long(sample_word_one)}")
    print(f"'{sample_word_two}' is long: {is_long(sample_word_two)}")