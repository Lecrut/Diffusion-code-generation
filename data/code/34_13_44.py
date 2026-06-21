class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_first_letter(self):
        if not isinstance(self.input_string, str):
            raise ValueError("Input must be a string")
        return self.input_string[0].upper() + self.input_string[1:] if self.input_string else ''

if __name__ == '__main__':
    sample_string = "good morning"
    manipulator = StringManipulator(sample_string)
    capitalized_string = manipulator.capitalize_first_letter()
    print(capitalized_string)