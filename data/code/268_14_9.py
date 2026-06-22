def get_first_word(words):
    words_list = words.split()
    if words_list:
        return words_list[0]
    else:
        raise ValueError("Input must be a non-empty string")

if __name__ == '__main__':
    sample_words = "   Hello world from Qwen  "
    try:
        print(get_first_word(sample_words))
    except ValueError as e:
        print(e)