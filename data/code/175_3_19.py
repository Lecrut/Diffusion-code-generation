def separate_words(text):
    words = [word for word in text.split() if word]
    return words

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with various spaces and punctuation."
    sample_string2 = "  \tWord1... Word2? End."
    sample_string3 = "OnlyWords"
    print(separate_words(sample_string1))
    print(separate_words(sample_string2))
    print(separate_words(sample_string3))