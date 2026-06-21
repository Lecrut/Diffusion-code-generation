def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ''.join(reversed(s))

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return reverse_string(self.input_string)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "12345",
        "Python"
    ]
    for s in sample_strings:
        manipulator = StringManipulator(s)
        print(manipulator.reverse())