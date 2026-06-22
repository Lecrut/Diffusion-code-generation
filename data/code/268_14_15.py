def get_first_word(words):
    return words.split()[0]

if __name__ == '__main__':
    sample_words = "Hello   world from Qwen"
    print(get_first_word(sample_words))