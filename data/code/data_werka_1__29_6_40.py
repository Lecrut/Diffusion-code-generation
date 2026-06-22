class WordReverser:
    def __init__(self, word):
        self.word = word

    def reverse(self):
        return self.word[::-1]

if __name__ == '__main__':
    sample_word = "Alibaba"
    reverser = WordReverser(sample_word)
    print(reverser.reverse())