class StringCaseConverter:
    def __init__(self, text: str):
        self.text = text

    def to_lowercase(self) -> str:
        return self.text.lower()

    def swap_case(self) -> str:
        return self.text.swapcase()

if __name__ == '__main__':
    sample_string = "Hello World"
    converter = StringCaseConverter(sample_string)
    lowercased = converter.to_lowercase()
    swapped = converter.swap_case()
    print(f"Original: {sample_string}")
    print(f"Lowercased: {lowercased}")
    print(f"Swapped Case: {swapped}")