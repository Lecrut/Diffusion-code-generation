class StringReverser:
    def reverse(self, word):
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        return ''.join(reversed(word))

if __name__ == '__main__':
    reverser = StringReverser()
    test_words = ["hello", "world", "Python"]
    for word in test_words:
        original = word
        reversed_word = reverser.reverse(word)
        print(f"Original: {original}, Reversed: {reversed_word}")