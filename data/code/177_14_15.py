class StringSplitter:
    WHITESPACES = " \t\n\r\f\v"

    @staticmethod
    def split_string_to_words(text):
        words = []
        word = []
        for char in text:
            if char in StringSplitter.WHITESPACES and word:
                words.append(''.join(word))
                word.clear()
            else:
                word.append(char)
        if word:
            words.append(''.join(word))
        return words

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "  hello world  "
    result1 = splitter.split_string_to_words(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")
    
    sample2 = "multiple   spaces here"
    result2 = splitter.split_string_to_words(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")
    
    sample3 = " leading and trailing "
    result3 = splitter.split_string_to_words(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")
    
    sample4 = ""
    result4 = splitter.split_string_to_words(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")