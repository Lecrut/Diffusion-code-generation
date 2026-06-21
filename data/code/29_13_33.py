def reverse_string(s):
    return ''.join(reversed(s))

class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def get_reversed(self):
        return reverse_string(self.input_string)
    
    def get_length(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "12345",
        "Python"
    ]
    for value in sample_values:
        processor = StringProcessor(value)
        print(f"Original: {value} -> Reversed: {processor.get_reversed()}, Length: {processor.get_length()}")