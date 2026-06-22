class StringManipulator:
    def __init__(self, text):
        self.text = text

    def capitalize_first_letter(self):
        if not isinstance(self.text, str):
            raise ValueError("Input must be a string")
        return self.text[0].upper() + self.text[1:] if self.text else ''

if __name__ == '__main__':
    sample_string = "hello world"
    manipulator = StringManipulator(sample_string)
    capitalized_string = manipulator.capitalize_first_letter()
    print(capitalized_string)