class StringManipulator:
    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        self.s = s

    def capitalize_first_letter(self):
        if not self.s:
            return ""
        first_char = self.s[0].upper()
        rest_of_string = self.s[1:]
        return first_char + rest_of_string

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "HELLO WORLD",
        "hello WORLD",
        "hElLo WoRlD",
        "",
        "a",
        "123abc",
        "!@#abc"
    ]
    for value in sample_values:
        manipulator = StringManipulator(value)
        print(manipulator.capitalize_first_letter())