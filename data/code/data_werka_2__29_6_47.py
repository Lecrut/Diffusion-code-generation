class StringReverser:
    def reverse_string(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return ''.join(reversed(input_string))

if __name__ == '__main__':
    sample_values = [
        "hello",
        "world",
        "Python3.8",
        "!@#$%",
        "12345",
        None,
        12345
    ]
    reverser = StringReverser()
    for value in sample_values:
        try:
            print(reverser.reverse_string(value))
        except ValueError as e:
            print(e)