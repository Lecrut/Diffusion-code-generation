class CaseConverter:
    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "HeLlO WoRlD"
    converter = CaseConverter(sample_string)
    
    lower_case = converter.to_lower()
    upper_case = converter.to_upper()
    title_case = converter.to_title()

    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Titlecase: {title_case}")