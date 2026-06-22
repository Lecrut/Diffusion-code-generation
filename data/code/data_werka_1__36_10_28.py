class StringReverser:
    def __init__(self):
        self.reversed_text = ""

    def _is_valid_input(self, text):
        return isinstance(text, str)

    def reverse(self, text):
        if not self._is_valid_input(text):
            raise ValueError("Input must be a string")
        self.reversed_text = ''.join(reversed(text))
        return self.reversed_text

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "Python is great.",
        "",
        "!dlroW ,olleH"
    ]
    
    reverser = StringReverser()
    for value in sample_values:
        print(reverser.reverse(value))