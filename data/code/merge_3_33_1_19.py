class StringProcessor:
    def remove_spaces(self, text: str) -> str:
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            text (str): The input string potentially containing spaces.
            
        Returns:
            str: A new string with all spaces removed.
        """
        return ''.join(char for char in text if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    test_cases = [
        "Hello World",
        "Python 3.10 is great ",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesAtAll"
    ]

    processor = StringProcessor()

    for i, original in enumerate(test_cases):
        result = processor.remove_spaces(original)
        print(f"Test Case {i + 1}:")
        print(f"Input:    '{original}'")
        print(f"Output:   '{result}'")
        print("-" * 30)