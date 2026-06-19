class StringReverser:
    def reverse(self, text):
        reversed_text = []
        for char in text:
            reversed_text.insert(0, char)
        return ''.join(reversed_text)

if __name__ == '__main__':
    reverser = StringReverser()
    SAMPLE_STRING_1 = "hello"
    SAMPLE_STRING_2 = "world"
    SAMPLE_STRING_3 = "Python"

    REVERSED_STRING_1 = reverser.reverse(SAMPLE_STRING_1)
    REVERSED_STRING_2 = reverser.reverse(SAMPLE_STRING_2)
    REVERSED_STRING_3 = reverser.reverse(SAMPLE_STRING_3)

    print(f"Original: {SAMPLE_STRING_1}, Reversed: {REVERSED_STRING_1}")
    print(f"Original: {SAMPLE_STRING_2}, Reversed: {REVERSED_STRING_2}")
    print(f"Original: {SAMPLE_STRING_3}, Reversed: {REVERSED_STRING_3}")