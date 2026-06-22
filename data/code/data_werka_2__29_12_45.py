class WordReverser:
    def __init__(self, word):
        self.word = word

    @staticmethod
    def reverse(word):
        reversed_word = []
        for i in range(len(word) - 1, -1, -1):
            reversed_word.append(word[i])
        return ''.join(reversed_word)

if __name__ == '__main__':
    sample_word = "optimization"
    reverser = WordReverser(sample_word)
    print(WordReverser.reverse(sample_word))