def first_word(words):
    return words.split()[0]

if __name__ == '__main__':
    sample_words = "   hello world   "
    print(first_word(sample_words))