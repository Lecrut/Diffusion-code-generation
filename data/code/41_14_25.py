class StringTransformer:
    def __init__(self, input_string):
        self.original = input_string

    def to_upper(self):
        return ''.join(char.upper() for char in self.original)

    def to_lower(self):
        return ''.join(char.lower() for char in self.original)

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    transformer = StringTransformer(sample_string)
    print(f"Original: {sample_string}")
    print(f"Uppercase: {transformer.to_upper()}")
    print(f"Lowercase: {transformer.to_lower()}")