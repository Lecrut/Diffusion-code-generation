class StringCaseManipulator:
    def transform(self, text):
        return text

    def to_lower(self, text):
        return self.transform(text).lower()

    def to_upper(self, text):
        return self.transform(text).upper()

    def to_title(self, text):
        return self.transform(text).title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = "Python Programming 101"
    original_text = sample_string
    lower_case = manipulator.to_lower(original_text)
    upper_case = manipulator.to_upper(original_text)
    title_case = manipulator.to_title(original_text)

    print(f"Original: {original_text}")
    print(f"Lowercase: {lower_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Title Case: {title_case}")