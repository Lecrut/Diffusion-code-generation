class WordReverser:
    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        self.word = word

    def reverse(self):
        return self.word[::-1]

if __name__ == '__main__':
    sample_word = "example"
    reverser = WordReverser(sample_word)
    reversed_word = reverser.reverse()
    print(reversed_word)