def get_first_word(words):
    return words[0] if words else None

if __name__ == '__main__':
    sample_words = ["Hello", "world"]
    print(get_first_word(sample_words))