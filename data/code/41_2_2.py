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
    sample_string = "Hello World Example"
    lower_case = manipulator.to_lower(sample_string)
    upper_case = manipulator.to_upper(sample_string)
    title_case = manipulator.to_title(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Title Case: {title_case}")