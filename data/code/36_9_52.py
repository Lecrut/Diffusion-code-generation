class StringReverser:
    REVERSE_CHARS = {chr(i): chr(255 - i) for i in range(128)}
    
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        reversed_text = []
        for char in text:
            reversed_text.append(StringReverser.REVERSE_CHARS.get(char, char))
        return ''.join(reversed_text)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Hello, World!"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)