class StringReverser:
    def __init__(self):
        self.reverse_lookup = {chr(i): chr(127 - i) for i in range(128)}
    
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        reversed_chars = []
        for char in text:
            if ord(char) < 128:
                reversed_chars.append(self.reverse_lookup[char])
            else:
                reversed_chars.append(char)
        
        return ''.join(reversed_chars)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Hello, World!"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)