class WordReverser:
    def reverse(self, s):
        return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    reverser = WordReverser()
    test_string = "The quick brown fox"
    print(reverser.reverse(test_string))