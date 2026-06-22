class StringReverser:
    def reverse(self, word):
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    SAMPLE_WORD_1 = "hello"
    SAMPLE_WORD_2 = "world"
    SAMPLE_WORD_3 = "Python"

    reverser = StringReverser()

    reversed_sample_1 = reverser.reverse(SAMPLE_WORD_1)
    print(f"Original: {SAMPLE_WORD_1}, Reversed: {reversed_sample_1}")

    reversed_sample_2 = reverser.reverse(SAMPLE_WORD_2)
    print(f"Original: {SAMPLE_WORD_2}, Reversed: {reversed_sample_2}")

    reversed_sample_3 = reverser.reverse(SAMPLE_WORD_3)
    print(f"Original: {SAMPLE_WORD_3}, Reversed: {reversed_sample_3}")