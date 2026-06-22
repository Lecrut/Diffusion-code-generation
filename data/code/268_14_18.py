def get_first_word(words):
    words_list = words.split()
    if not words_list:
        raise ValueError("Input must contain at least one word")
    return words_list[0]

if __name__ == '__main__':
    sample_words = "Hello   world this is a test"
    try:
        first_word = get_first_word(sample_words)
        print(first_word)
    except ValueError as e:
        print(e)