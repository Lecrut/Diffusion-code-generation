class StringManipulator:
    def __init__(self):
        self.translator = str.maketrans('', '', ' ')

    def remove_spaces(self, s):
        return s.translate(self.translator)

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string = "Hello, World! This is a test."
    result = manipulator.remove_spaces(sample_string)
    print(result)