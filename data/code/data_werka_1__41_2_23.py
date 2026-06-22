class StringCaseManipulator:
    def __init__(self):
        self.text = ""

    def transform(self, text):
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = "Hello World This Is A Test"
    manipulator.transform(sample_string)
    print("Original:", sample_string)
    print("Lowercase:", manipulator.to_lower())
    print("Uppercase:", manipulator.to_upper())
    print("Title Case:", manipulator.to_title())