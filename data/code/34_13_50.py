class StringManipulator:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def capitalize_first_letter(self):
        if not self.input_string:
            return self.input_string
        return self.input_string[0].upper() + self.input_string[1:]

if __name__ == '__main__':
    sample_string = "hello world"
    manipulator = StringManipulator(sample_string)
    capitalized_string = manipulator.capitalize_first_letter()
    print(capitalized_string)

    another_sample = "good morning"
    another_manipulator = StringManipulator(another_sample)
    another_capitalized_string = another_manipulator.capitalize_first_letter()
    print(another_capitalized_string)