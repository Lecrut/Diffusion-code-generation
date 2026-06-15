def is_word_long(word, min_length):
    return len(word) >= min_length
if __name__ == '__main__':
    sample_word = "programming"
    minimum_length = 7
    result = is_word_long(sample_word, minimum_length)
    print(f"Word: {sample_word}")
    print(f"Minimum Length: {minimum_length}")
    print(f"Is the word long? {result}")
    sample_word_short = "code"
    result_short = is_word_long(sample_word_short, minimum_length)
    print(f"\nWord: {sample_word_short}")
    print(f"Minimum Length: {minimum_length}")
    print(f"Is the word long? {result_short}")