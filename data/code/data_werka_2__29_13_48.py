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
    sample_values = [
        "Alibaba Cloud",
        "Python Programming",
        "Reverse Me"
    ]
    for value in sample_values:
        manipulator = StringManipulator(value)
        print(f"Original: {value} -> Reversed: {manipulator.get_reversed()}")