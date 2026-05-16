class StringCaseManipulator:
    def transform(self, text):
        return text
    def to_lower(self, text):
        return text.lower()
    def to_upper(self, text):
        return text.upper()
    def to_title(self, text):
        return text.title()
if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_text = "Hello World This Is A Test"
    print("Original Text:", sample_text)
    print("Lowercase:", manipulator.to_lower(sample_text))
    print("Uppercase:", manipulator.to_upper(sample_text))
    print("Title Case:", manipulator.to_title(sample_text))