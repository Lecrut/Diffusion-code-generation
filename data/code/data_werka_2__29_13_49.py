def reverse_string(s):
    return ''.join(reversed(s))

class StringManipulator:
    REVERSE_METHOD = reverse_string

    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def reverse_helper(s):
        return StringManipulator.REVERSE_METHOD(s)

    def get_reversed(self):
        return self.reverse_helper(self.input_string)

if __name__ == '__main__':
    sample_values = [
        "Alibaba Cloud",
        "Python Programming",
        "OpenAI ChatGPT"
    ]
    for value in sample_values:
        manipulator = StringManipulator(value)
        print(f"Original: {value} -> Reversed: {manipulator.get_reversed()}")