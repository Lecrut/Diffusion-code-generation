class StringSplitter:
    WHITESPACE_CHARS = " \t\n\r\f\v"

    @staticmethod
    def split_by_whitespace(text):
        words = []
        word = ""
        for char in text:
            if char in StringSplitter.WHITESPACE_CHARS:
                if word:
                    words.append(word)
                    word = ""
            else:
                word += char
        if word:
            words.append(word)
        return words

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "  hello world  "
    result1 = splitter.split_by_whitespace(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")
    sample2 = "multiple   spaces here"
    result2 = splitter.split_by_whitespace(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")
    sample3 = " leading and trailing "
    result3 = splitter.split_by_whitespace(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")
    sample4 = ""
    result4 = splitter.split_by_whitespace(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")