class CaseConverter:
    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return ''.join([char.lower() for char in self.text])

    def to_upper(self):
        return ''.join([char.upper() for char in self.text])

    def to_title(self):
        return ''.join([char.title() if i == 0 else char.lower() for i, char in enumerate(self.text)])

if __name__ == '__main__':
    SAMPLE_STRING = "HeLlO WoRlD"
    converter = CaseConverter(SAMPLE_STRING)
    print(f"Original: {SAMPLE_STRING}")
    print(f"Lowercase: {converter.to_lower()}")
    print(f"Uppercase: {converter.to_upper()}")
    print(f"Titlecase: {converter.to_title()}")