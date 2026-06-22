def get_first_word(words_list):
    if words_list:
        return words_list[0]
    else:
        return ""

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry"]
    print(f"First word: '{get_first_word(sample_words)}'")

    empty_list = []
    print(f"First word (empty list): '{get_first_word(empty_list)}'")