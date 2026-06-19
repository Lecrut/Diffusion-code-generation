class StringCaseManipulator:
    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

    def switch_case(self, case_type):
        if case_type == 'lower':
            return self.to_lower()
        elif case_type == 'upper':
            return self.to_upper()
        elif case_type == 'title':
            return self.to_title()
        else:
            raise ValueError("Invalid case type. Use 'lower', 'upper', or 'title'.")

if __name__ == '__main__':
    sample_text = "HeLlO WoRlD"
    manipulator = StringCaseManipulator(sample_text)
    
    print(f"Original: {sample_text}")
    print(f"Lowercase: {manipulator.switch_case('lower')}")
    print(f"Uppercase: {manipulator.switch_case('upper')}")
    print(f"Titlecase: {manipulator.switch_case('title')}")