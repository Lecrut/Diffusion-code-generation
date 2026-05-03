class StringManipulator:
    def to_lower(self, text: str) -> str:
        return text.lower()
    def to_upper(self, text: str) -> str:
        return text.upper()
    def to_title(self, text: str) -> str:
        return text.title()
    def swap_case(self, text: str) -> str:
        return text.swapcase()
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string = "HeLlO wOrLd"
    print(f"Original: {sample_string}")
    print(f"Lowercase: {manipulator.to_lower(sample_string)}")
    print(f"Uppercase: {manipulator.to_upper(sample_string)}")
    print(f"Title Case: {manipulator.to_title(sample_string)}")
    print(f"Swap Case: {manipulator.swap_case(sample_string)}")