class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_first_letter(self):
        return ' '.join(word.capitalize() for word in self.input_string.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    manipulator = StringManipulator(sample_string)
    capitalized_string = manipulator.capitalize_first_letter()
    print(capitalized_string)