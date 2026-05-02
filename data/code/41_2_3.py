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
    lower_case = manipulator.to_lower(sample_text)
    upper_case = manipulator.to_upper(sample_text)
    title_case = manipulator.to_title(sample_text)
    print(f"Original: {sample_text}")
    print(f"Lowercase: {lower_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Title Case: {title_case}")