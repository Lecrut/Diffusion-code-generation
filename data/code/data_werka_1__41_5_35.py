class StringCaseManipulator:
    @classmethod
    def switch_case(cls, text, case_type):
        if case_type == 'lower':
            return text.lower()
        elif case_type == 'upper':
            return text.upper()
        elif case_type == 'title':
            return text.title()
        else:
            raise ValueError("Invalid case type. Use 'lower', 'upper', or 'title'.")

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(StringCaseManipulator.switch_case(sample_text, 'lower'))
    print(StringCaseManipulator.switch_case(sample_text, 'upper'))
    print(StringCaseManipulator.switch_case(sample_text, 'title'))