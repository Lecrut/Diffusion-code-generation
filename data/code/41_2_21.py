class StringCaseManipulator:
    def transform(self, text, case):
        cases = {
            'lower': self.to_lower,
            'upper': self.to_upper,
            'title': self.to_title
        }
        if case in cases:
            return cases[case](text)
        raise ValueError("Unsupported case type")

    def to_lower(self, text):
        return text.lower()

    def to_upper(self, text):
        return text.upper()

    def to_title(self, text):
        return text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = "Hello World This Is A Test"
    print("Original:", sample_string)
    print("Lowercase:", manipulator.transform(sample_string, 'lower'))
    print("Uppercase:", manipulator.transform(sample_string, 'upper'))
    print("Title Case:", manipulator.transform(sample_string, 'title'))