def find_first_word(words):
    return words.split(maxsplit=1)[0]

if __name__ == '__main__':
    sample_words = "Hello   world from Qwen"
    print(find_first_word(sample_words))