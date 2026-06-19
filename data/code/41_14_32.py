def to_upper(s: str) -> str:
    return ''.join(c.upper() if 'a' <= c <= 'z' else c for c in s)

def to_lower(s: str) -> str:
    return ''.join(c.lower() if 'A' <= c <= 'Z' else c for c in s)

class StringTransformer:
    def __init__(self, input_string: str):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def transform_to_upper(self) -> str:
        return to_upper(self.input_string)

    def transform_to_lower(self) -> str:
        return to_lower(self.input_string)

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    transformer = StringTransformer(sample_string)
    print(f"Original: {sample_string}")
    print(f"Uppercase: {transformer.transform_to_upper()}")
    print(f"Lowercase: {transformer.transform_to_lower()}")