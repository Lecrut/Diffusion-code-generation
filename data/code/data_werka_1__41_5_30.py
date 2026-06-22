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
    sample_string = "Python Programming"
    converter = CaseConverter(sample_string)
    
    lowercase_result = converter.to_lower()
    uppercase_result = converter.to_upper()
    titlecase_result = converter.to_title()

    print(f"Original: {sample_string}")
    print(f"Lowercase: {lowercase_result}")
    print(f"Uppercase: {uppercase_result}")
    print(f"Titlecase: {titlecase_result}")