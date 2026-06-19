class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return self._reverse_string(text)

    def _reverse_string(self, text):
        reversed_text = ""
        for char in text:
            reversed_text = char + reversed_text
        return reversed_text

if __name__ == '__main__':
    reverser = StringReverser()
    sample_strings = ["hello", "world", "Python"]
    for original in sample_strings:
        try:
            reversed_string = reverser.reverse(original)
            print(f"Original: {original}, Reversed: {reversed_string}")
        except ValueError as e:
            print(e)