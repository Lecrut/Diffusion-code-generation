class StringReverser:
    def reverse(self, word):
        return word[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample_word = "hello world"
    reversed_word = reverser.reverse(sample_word)
    print(reversed_word)