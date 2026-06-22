def is_long(word):
    return len(word) > 10
if __name__ == '__main__':
    sample_word_short = 'hello'
    sample_word_long = 'this is a very long string'
    print(f"Is '{sample_word_short}' long? {is_long(sample_word_short)}")
    print(f"Is '{sample_word_long}' long? {is_long(sample_word_long)}")