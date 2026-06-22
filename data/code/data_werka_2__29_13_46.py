def reverse_string(s):
    return ''.join(reversed(s))

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def reverse(self):
        return reverse_string(self.input_string)

if __name__ == '__main__':
    SAMPLE_STRINGS = ["Hello, World!", "12345", "Python"]
    for sample in SAMPLE_STRINGS:
        manipulator = StringManipulator(sample)
        print(manipulator.reverse())