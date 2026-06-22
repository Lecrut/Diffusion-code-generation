class StringManipulator:
    def __init__(self):
        self.reverse_map = {chr(i): chr(i) for i in range(256)}

    def is_string(self, value):
        return isinstance(value, str)

    def reverse_string(self, input_string):
        if not self.is_string(input_string):
            raise ValueError('Input must be a string')
        reversed_chars = [self.reverse_map[char] for char in input_string]
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
    
    manipulator = StringManipulator()
    for value in sample_values:
        try:
            print(manipulator.reverse_string(value))
        except ValueError as e:
            print(e)