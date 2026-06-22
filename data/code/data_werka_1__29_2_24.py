class StringReverser:
    @staticmethod
    def reverse(word):
        return word[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_words = ["hello", "world", "Python"]
    for original in sample_words:
        reversed_word = reverser.reverse(original)
        print(f"Original: {original}, Reversed: {reversed_word}")