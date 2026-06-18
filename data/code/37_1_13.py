class StringManipulator:
    def __init__(self, string1: str = "", string2: str = "") -> None:
        """Initialize with optional default strings."""
        self.string_a = string1
        self.string_b = string2
    
    def combine_strings(self) -> str:
        """Combine two internal variables into a single string.
        
        Returns:
            The concatenated result of the two strings.
        """
        combined_string = f"{self.string_a}{self.string_b}"
        return combined_string

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    
    manipulator_1 = StringManipulator("Hello ", "World!")
    result_1 = manipulator_1.combine_strings()
    
    manipulator_2 = StringManipulator("", "")  # Test with empty defaults
    result_2 = manipulator_2.combine_strings()
    
    print(result_1)   # Expected output: Hello World!
    print(repr(result_2))  # Expected output: ''