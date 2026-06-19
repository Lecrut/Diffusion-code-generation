class StringReverser:
    def __init__(self):
        self.REVERSE_DIRECTION = -1

    def reverse(self, text):
        return text[::self.REVERSE_DIRECTION]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_strings = ["hello", "world", "Python"]
    for original in sample_strings:
        reversed_string = reverser.reverse(original)
        print(f"Original: {original}, Reversed: {reversed_string}")