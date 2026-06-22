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
    sample_string = "Python Programming Language"
    
    original_text = sample_string
    lower_case_text = manipulator.to_lower(original_text)
    upper_case_text = manipulator.to_upper(original_text)
    title_case_text = manipulator.to_title(original_text)

    print(f"Original: {original_text}")
    print(f"Lowercase: {lower_case_text}")
    print(f"Uppercase: {upper_case_text}")
    print(f"Title Case: {title_case_text}")