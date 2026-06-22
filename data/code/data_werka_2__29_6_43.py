class StringProcessor:

    def __init__(self):
        self.reverse_map = {chr(i): chr(i) for i in range(256)}

    def reverse_string(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError('Input must be a string')
        reversed_chars = [self.reverse_map[char] for char in input_string]
        return ''.join(reversed_chars[::-1])
if __name__ == '__main__':
    sample_values = ['hello', 'world', 'Python', '12345', '!@#$%', 12345, None]
    processor = StringProcessor()
    for value in sample_values:
        try:
            print(processor.reverse_string(value))
        except ValueError as e:
            print(e)