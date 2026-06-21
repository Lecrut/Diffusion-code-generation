class TextSplitter:

    @staticmethod
    def separate_words(text):
        return [word for word in text.strip().split()]
if __name__ == '__main__':
    splitter = TextSplitter()
    test_string1 = '  hello world  '
    result1 = splitter.separate_words(test_string1)
    print(f"Input: '{test_string1}'")
    print(f'Output: {result1}')
    test_string2 = 'multiple   spaces   here'
    result2 = splitter.separate_words(test_string2)
    print(f"Input: '{test_string2}'")
    print(f'Output: {result2}')
    test_string3 = ' leading and trailing '
    result3 = splitter.separate_words(test_string3)
    print(f"Input: '{test_string3}'")
    print(f'Output: {result3}')
    test_string4 = ''
    result4 = splitter.separate_words(test_string4)
    print(f"Input: '{test_string4}'")
    print(f'Output: {result4}')