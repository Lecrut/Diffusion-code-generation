class WordReverser:
    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    reverser = WordReverser()
    test_string = "hello world this is a test"
    print(reverser.reverse_words(test_string))