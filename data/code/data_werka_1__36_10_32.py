class StringReverser:
    def __init__(self):
        self.reversed_text = ""

    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self._reverse_string(text)
        return self.reversed_text

    def _reverse_string(self, s):
        reversed_chars = []
        for char in s:
            reversed_chars.insert(0, char)
        self.reversed_text = ''.join(reversed_chars)

if __name__ == '__main__':
    sample_values = ["hello world", "Python is great!", "", "!dlroW ,olleH"]
    string_reverser = StringReverser()
    for value in sample_values:
        print(f"Original: '{value}' -> Reversed: '{string_reverser.reverse(value)}'")