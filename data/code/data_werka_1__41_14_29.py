class StringTransformer:
    def __init__(self, input_string):
        self.input_string = input_string

    def to_upper(self):
        return self.input_string.upper()

    def to_lower(self):
        return self.input_string.lower()

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    transformer = StringTransformer(sample_string)
    print(f"Original: {sample_string}")
    print(f"Uppercase: {transformer.to_upper()}")
    print(f"Lowercase: {transformer.to_lower()}")