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
    lower_case = manipulator.to_lower(sample_string)
    upper_case = manipulator.to_upper(sample_string)
    title_case = manipulator.to_title(sample_string)
    swapped_case = manipulator.swap_case(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower_case}")
    print(f"Uppercase: {upper_case}")
    print(f"Title Case: {title_case}")
    print(f"Swapped Case: {swapped_case}")