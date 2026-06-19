class StringReverser:
    def reverse(self, text):
        reversed_text = ""
        for char in text:
            reversed_text = char + reversed_text
        return reversed_text

if __name__ == '__main__':
    SAMPLE_STRING_1 = "hello"
    SAMPLE_STRING_2 = "world"
    SAMPLE_STRING_3 = "Python"

    reverser = StringReverser()

    reversed_string_1 = reverser.reverse(SAMPLE_STRING_1)
    print(f"Original: {SAMPLE_STRING_1}, Reversed: {reversed_string_1}")

    reversed_string_2 = reverser.reverse(SAMPLE_STRING_2)
    print(f"Original: {SAMPLE_STRING_2}, Reversed: {reversed_string_2}")

    reversed_string_3 = reverser.reverse(SAMPLE_STRING_3)
    print(f"Original: {SAMPLE_STRING_3}, Reversed: {reversed_string_3}")