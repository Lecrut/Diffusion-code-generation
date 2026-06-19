class StringCaseConverter:
    CASE_MAP = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title
    }

    def __init__(self, text):
        self.text = text

    def convert_case(self, case_type):
        if case_type in self.CASE_MAP:
            return self.CASE_MAP[case_type](self.text)
        else:
            raise ValueError("Invalid case type. Use 'lower', 'upper', or 'title'.")

if __name__ == '__main__':
    sample_string = "HeLlO WoRlD"
    converter = StringCaseConverter(sample_string)
    
    lower_case = converter.convert_case('lower')
    upper_case = converter.convert_case('upper')
    title_case = converter.convert_case('title')
    
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Titlecase: {title_case}")