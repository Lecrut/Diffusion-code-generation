class StringReverser:
    def __init__(self):
        self.reversed_string = ""
    
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.reversed_string = ''.join(char for char in reversed(text))
        return self.reversed_string

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text1 = "Hello, World!"
    sample_text2 = "Alibaba Cloud"
    
    reversed_text1 = reverser.reverse(sample_text1)
    print(reversed_text1)
    
    reversed_text2 = reverser.reverse(sample_text2)
    print(reversed_text2)