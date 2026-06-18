class StringManipulator:
    def __init__(self, str1: str = "", str2: str = "") -> None:
        """Initialize internal string variables."""
        self.str1 = str1
        self.str2 = str2

    def combine_strings(self) -> str:
        """Combine the two internal strings into a single string."""
        return f"{self.str1}{self.str2}"

if __name__ == "__main__":
    # Hard-coded sample values for testing without user input or external dependencies
    manipulator = StringManipulator(str1="Hello", str2="World")
    result = manipulator.combine_strings()
    
    print("Combined string:", result)

    # Additional test case with empty strings to ensure robustness
    manipulator2 = StringManipulator("")
    result2 = manipulator2.combine_strings()
    print("Test 2 - Empty input combined (default):", repr(result2))