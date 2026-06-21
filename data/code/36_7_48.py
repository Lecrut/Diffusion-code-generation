class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

    def get_input(self):
        return self.input_string

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    manipulator = StringManipulator(sample_string)
    print(manipulator.reverse())
    print(manipulator.get_input())