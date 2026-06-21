class SentenceSplitter:
    WHITESPACE_DELIMITERS = ' \t\n'

    @staticmethod
    def split_sentence(text):
        return text.split(SentenceSplitter.WHITESPACE_DELIMITERS)

if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_string1 = "  hello world  "
    result1 = splitter.split_sentence(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: {result1}")

    test_string2 = "multiple   spaces   here"
    result2 = splitter.split_sentence(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: {result2}")

    test_string3 = "singleword"
    result3 = splitter.split_sentence(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: {result3}")

    test_string4 = "   leading and trailing spaces   "
    result4 = splitter.split_sentence(test_string4)
    print(f"Input: '{test_string4}'")
    print(f"Output: {result4}")