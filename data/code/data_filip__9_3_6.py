class DataValidator:
    def clean_input(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.strip()

if __name__ == '__main__':
    validator = DataValidator()
    sample_input = "   hello world   "
    cleaned = validator.clean_input(sample_input)
    print(cleaned)