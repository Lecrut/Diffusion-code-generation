class WordReverser:
    def __init__(self, word):
        self.word = word

    @staticmethod
    def reverse_string(s):
        return s[::-1]

    def get_reversed_word(self):
        return self.reverse_string(self.word)

if __name__ == '__main__':
    sample_word = "Alibaba Cloud"
    reverser = WordReverser(sample_word)
    reversed_word = reverser.get_reversed_word()
    print(reversed_word)