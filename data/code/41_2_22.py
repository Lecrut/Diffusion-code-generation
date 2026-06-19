class StringCaseManipulator:
    def transform(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text

    def to_lower(self, text):
        return self.transform(text).lower()

    def to_upper(self, text):
        return self.transform(text).upper()

    def to_title(self, text):
        return self.transform(text).title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = "Hello World This Is A Test"
    print("Original:", sample_string)
    try:
        print("Lowercase:", manipulator.to_lower(sample_string))
        print("Uppercase:", manipulator.to_upper(sample_string))
        print("Title Case:", manipulator.to_title(sample_string))
    except ValueError as e:
        print(e)