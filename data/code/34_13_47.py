class StringManipulator:
    def __init__(self, text):
        self.text = text

    def capitalize_first_letter(self):
        if not isinstance(self.text, str):
            raise ValueError("Input must be a string")
        return self.text.capitalize()

if __name__ == '__main__':
    sample_string = "hello world"
    manipulator = StringManipulator(sample_string)
    capitalized_string = manipulator.capitalize_first_letter()
    print(capitalized_string)

    another_sample = "good morning"
    another_manipulator = StringManipulator(another_sample)
    another_capitalized_string = another_manipulator.capitalize_first_letter()
    print(another_capitalized_string)