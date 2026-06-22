def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

class StringReverser:
    def __init__(self, text):
        self.text = text
    
    def get_reversed_text(self):
        try:
            return reverse_string(self.text)
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        12345,
        "Alibaba Cloud",
        "Python Programming"
    ]
    
    for original in sample_texts:
        reverser = StringReverser(original)
        result = reverser.get_reversed_text()
        print(f"Original: {original}, Reversed: {result}")