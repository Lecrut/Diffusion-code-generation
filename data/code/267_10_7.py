def is_word_long(word, min_length):
    return len(word) >= min_length
if __name__ == '__main__':
    sample_word = "programming"
    min_len_setting = 7
    result = is_word_long(sample_word, min_len_setting)
    print(f"Word: {sample_word}, Minimum Length: {min_len_setting}")
    print(f"Is the word long? {result}")
    sample_word_short = "code"
    result_short = is_word_long(sample_word_short, min_len_setting)
    print(f"Word: {sample_word_short}, Minimum Length: {min_len_setting}")
    print(f"Is the word long? {result_short}")
    sample_word_long = "supercalifragilisticexpialidocious"
    result_long = is_word_long(sample_word_long, min_len_setting)
    print(f"Word: {sample_word_long}, Minimum Length: {min_len_setting}")
    print(f"Is the word long? {result_long}")