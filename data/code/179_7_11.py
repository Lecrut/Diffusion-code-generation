def reverse_word_order(s):
    WORD_DELIMITER = " "
    words = s.split(WORD_DELIMITER)
    reversed_words = words[::-1]
    return WORD_DELIMITER.join(reversed_words)

if __name__ == '__main__':
    sample_string = "Data Science is fun"
    result = reverse_word_order(sample_string)
    print(result)