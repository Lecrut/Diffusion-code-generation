class StringReverser:
    def __init__(self):
        self.REVERSED_SUFFIX = "_reversed"

    def reverse(self, word):
        reversed_word = ''.join(reversed(word))
        return f"{reversed_word}{self.REVERSED_SUFFIX}"

if __name__ == '__main__':
    reverser = StringReverser()
    sample_word1 = "hello"
    print(reverser.reverse(sample_word1))
    sample_word2 = "world"
    print(reverser.reverse(sample_word2))
    sample_word3 = "Python"
    print(reverser.reverse(sample_word3))