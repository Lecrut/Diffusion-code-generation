class StringReverser:
    def __init__(self):
        self.supported_types = (str,)
    
    def validate_input(self, text):
        if not isinstance(text, self.supported_types):
            raise ValueError("Input must be a string")
    
    def reverse(self, text):
        self.validate_input(text)
        reversed_text = []
        for char in reversed(text):
            reversed_text.append(char)
        return ''.join(reversed_text)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Alibaba Cloud"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)