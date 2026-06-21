class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_first_letter(self):
        if not self.input_string:
            return self.input_string
        stripped_s = self.input_string.strip()
        if not stripped_s:
            return self.input_string
        capitalized_s = stripped_s[0].upper() + stripped_s[1:]
        leading_spaces = len(self.input_string) - len(stripped_s)
        trailing_spaces = len(self.input_string) - len(stripped_s) - leading_spaces
        return ' ' * leading_spaces + capitalized_s + ' ' * trailing_spaces

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "  hello world  ",
        "",
        "hELLO",
        "123abc",
        "   ",
        "a",
        "multiple   spaces"
    ]
    for value in sample_values:
        manipulator = StringManipulator(value)
        print(manipulator.capitalize_first_letter())