class WordReverser:
    def __init__(self, word):
        self.word = word

    @staticmethod
    def reverse_string(s):
        reversed_chars = []
        for i in range(len(s) - 1, -1, -1):
            reversed_chars.append(s[i])
        return ''.join(reversed_chars)

    def get_reversed_word(self):
        return self.reverse_string(self.word)

if __name__ == '__main__':
    sample_word = "hello"
    reverser = WordReverser(sample_word)
    print(reverser.get_reversed_word())