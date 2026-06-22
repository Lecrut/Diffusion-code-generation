class StringReverser:
    def __init__(self):
        self.reverse_stack = []

    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.reverse_stack.clear()
        for char in text:
            self.reverse_stack.append(char)
        return ''.join(reversed(self.reverse_stack))

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text1 = "Hello, World!"
    sample_text2 = "Alibaba Cloud"
    reversed_text1 = reverser.reverse(sample_text1)
    print(reversed_text1)
    reversed_text2 = reverser.reverse(sample_text2)
    print(reversed_text2)