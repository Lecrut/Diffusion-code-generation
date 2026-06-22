class StringReverser:
    def __init__(self):
        self.reverse_stack = []

    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        for char in text:
            self.reverse_stack.append(char)
        
        reversed_text = ''.join(self.reverse_stack[::-1])
        return reversed_text

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text1 = "Hello, World!"
    sample_text2 = "Alibaba Cloud"
    
    reversed_text1 = reverser.reverse(sample_text1)
    print(reversed_text1)
    
    reversed_text2 = reverser.reverse(sample_text2)
    print(reversed_text2)