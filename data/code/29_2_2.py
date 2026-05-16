class StringReverser:
    def reverse(self, word):
        return word[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample_word_1 = "hello"
    reversed_word_1 = reverser.reverse(sample_word_1)
    print(f"Original: {sample_word_1}, Reversed: {reversed_word_1}")
    sample_word_2 = "world"
    reversed_word_2 = reverser.reverse(sample_word_2)
    print(f"Original: {sample_word_2}, Reversed: {reversed_word_2}")
    sample_word_3 = "Python"
    reversed_word_3 = reverser.reverse(sample_word_3)
    print(f"Original: {sample_word_3}, Reversed: {reversed_word_3}")