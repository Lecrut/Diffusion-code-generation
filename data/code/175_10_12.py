class SentenceSplitter:
    WHITESPACE_DELIMITERS = ' \t\n\r'

    @staticmethod
    def separate_words(text):
        return text.split(SentenceSplitter.WHITESPACE_DELIMITERS)

if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_string1 = "  hello world  "
    result1 = splitter.separate_words(test_string1)
    print(result1)
    test_string2 = "multiple   spaces here"
    result2 = splitter.separate_words(test_string2)
    print(result2)
    test_string3 = " leading and trailing "
    result3 = splitter.separate_words(test_string3)
    print(result3)
    test_string4 = ""
    result4 = splitter.separate_words(test_string4)
    print(result4)