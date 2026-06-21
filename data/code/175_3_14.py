class WordSeparator:
    def separate_words(self, text):
        return [word for word in text.split() if word]

if __name__ == '__main__':
    separator = WordSeparator()
    sample_string1 = "Hello world! This is a test, with various spaces and punctuation."
    sample_string2 = "  \tWord1... Word2? End."
    sample_string3 = "OnlyWords"
    print(separator.separate_words(sample_string1))
    print(separator.separate_words(sample_string2))
    print(separator.separate_words(sample_string3))