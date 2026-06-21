class WordReverser:
    def reverse_words(self, sentence):
        return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    reverser = WordReverser()
    test_string = "hello world this is a test"
    result = reverser.reverse_words(test_string)
    print(result)