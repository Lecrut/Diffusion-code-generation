class CaseConverter:
    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return ''.join([char.lower() for char in self.text])

    def to_upper(self):
        return ''.join([char.upper() for char in self.text])

    def to_title(self):
        words = self.text.split()
        titlecased_words = [word.capitalize() for word in words]
        return ' '.join(titlecased_words)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud Is Awesome"
    converter = CaseConverter(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {converter.to_lower()}")
    print(f"Uppercase: {converter.to_upper()}")
    print(f"Titlecase: {converter.to_title()}")