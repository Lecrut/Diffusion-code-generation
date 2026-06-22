class StringCaseConverter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def to_lower(self):
        return self.input_string.lower()

    def to_upper(self):
        return self.input_string.upper()

    def to_title(self):
        return self.input_string.title()

if __name__ == '__main__':
    sample_text = "HeLlO WoRlD"
    converter = StringCaseConverter(sample_text)
    print("Original:", sample_text)
    print("Lowercase:", converter.to_lower())
    print("Uppercase:", converter.to_upper())
    print("Titlecase:", converter.to_title())