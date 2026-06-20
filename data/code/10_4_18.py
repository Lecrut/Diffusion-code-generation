class WordOrderReverser:
    DEFAULT_SEPARATOR = ' '

    @staticmethod
    def reverse(text):
        if not text:
            return ''
        words = text.split()
        return WordOrderReverser.DEFAULT_SEPARATOR.join(words[::-1])

if __name__ == '__main__':
    test_cases = [
        "The quick brown fox",
        "Python 101",
        "a b c d e"
    ]
    reverser = WordOrderReverser()
    for case in test_cases:
        output = reverser.reverse(case)
        print(output)