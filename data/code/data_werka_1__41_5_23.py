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
    
    print(f"Original: {sample_string}")
    print(f"Lowercase: {converter.to_lower()}")
    print(f"Uppercase: {converter.to_upper()}")
    print(f"Titlecase: {converter.to_title()}")