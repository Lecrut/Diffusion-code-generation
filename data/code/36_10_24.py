class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return self._reverse_string(text)

    def _reverse_string(self, text):
        reversed_text = ''
        for char in text:
            reversed_text = char + reversed_text
        return reversed_text

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "Python is great.",
        "!dlroW ,olleH",
        "",
        "A man a plan a canal Panama"
    ]
    
    reverser = StringReverser()
    for value in sample_values:
        print(f"Original: {value}")
        print(f"Reversed: {reverser.reverse(value)}")