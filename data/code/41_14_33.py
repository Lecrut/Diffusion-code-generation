class StringTransformer:
    def __init__(self, input_string):
        self.original = input_string

    def to_upper(self):
        return ''.join(c.upper() for c in self.original)

    def to_lower(self):
        return ''.join(c.lower() for c in self.original)

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd ExAmPle"
    transformer = StringTransformer(sample_string)
    print(f"Original: {transformer.original}")
    print(f"Uppercase: {transformer.to_upper()}")
    print(f"Lowercase: {transformer.to_lower()}")