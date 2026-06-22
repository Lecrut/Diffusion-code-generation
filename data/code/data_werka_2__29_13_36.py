def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ''.join(reversed(s))

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_reversed(self):
        return reverse_string(self.input_string)

if __name__ == '__main__':
    SAMPLE_VALUES = [
        "Hello, World!",
        "12345",
        "Python"
    ]

    for value in SAMPLE_VALUES:
        try:
            manipulator = StringManipulator(value)
            print(f"Original: {value} -> Reversed: {manipulator.get_reversed()}")
        except ValueError as e:
            print(e)