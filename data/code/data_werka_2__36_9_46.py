class StringReverser:
    def __init__(self):
        self.reverse_map = {chr(i): chr(255 - i) for i in range(128)}
    
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        reversed_text = []
        for char in text:
            if ord(char) < 128:
                reversed_text.append(self.reverse_map[char])
            else:
                reversed_text.append(char)
        
        return ''.join(reversed_text[::-1])

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Hello, World!"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)