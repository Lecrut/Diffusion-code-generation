class StringProcessor:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ''.join(reversed(self.text))

    def length(self):
        return len(self.text)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    processor = StringProcessor(sample_string)
    reversed_string = processor.reverse()
    string_length = processor.length()
    
    print(reversed_string)
    print(string_length)