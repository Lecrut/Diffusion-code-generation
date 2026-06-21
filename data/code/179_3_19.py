class WordReverser:
    @staticmethod
    def reverse(s):
        return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    test_string = "The quick brown fox"
    result = WordReverser.reverse(test_string)
    print(result)