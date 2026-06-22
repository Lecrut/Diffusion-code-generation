class StringManipulator:
    def __init__(self, text):
        self.text = text

    def capitalize_first_letter(self):
        if not isinstance(self.text, str):
            raise ValueError("Input must be a string")
        if len(self.text) == 0:
            return self.text
        return self.text[0].upper() + self.text[1:]

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "Python", "", "a"]
    for value in sample_values:
        manipulator = StringManipulator(value)
        print(manipulator.capitalize_first_letter())