class StringReverser:
    def __init__(self):
        self.reverse_map = {chr(i): chr(i) for i in range(256)}

    def reverse_string(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        reversed_chars = [self.reverse_map[char] for char in input_string]
        return ''.join(reversed_chars[::-1])

if __name__ == '__main__':
    SAMPLE_VALUES = [
        "hello",
        "world",
        "Python3.8",
        "!@#$%",
        "12345",
        None
    ]
    reverser = StringReverser()
    for value in SAMPLE_VALUES:
        try:
            print(reverser.reverse_string(value))
        except ValueError as e:
            print(e)