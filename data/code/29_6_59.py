class StringReverser:
    def __init__(self):
        self.supported_chars = set(chr(i) for i in range(256))

    def is_string(self, value):
        return isinstance(value, str)

    def reverse_string(self, input_string):
        if not self.is_string(input_string):
            raise ValueError('Input must be a string')
        
        reversed_chars = []
        for char in input_string:
            if char not in self.supported_chars:
                raise ValueError(f'Unsupported character: {char}')
            reversed_chars.append(char)
        
        return ''.join(reversed_chars[::-1])

if __name__ == '__main__':
    sample_values = [
        "hello",
        "world",
        "Python3.8",
        "!@#$%",
        12345,
        None
    ]
    
    reverser = StringReverser()
    for value in sample_values:
        try:
            print(reverser.reverse_string(value))
        except ValueError as e:
            print(e)