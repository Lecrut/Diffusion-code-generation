class StringProcessor:
    def remove_spaces(self, s: str) -> str:
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            s (str): The input string containing potential whitespace characters.
            
        Returns:
            str: A new string with all space characters removed.
        """
        return ''.join(char for char in s if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    test_cases = [
        "Hello World",
        "Python 3.10 is great ",
        "   Multiple     spaces   here   ",
        "",
        "NoSpacesHere"
    ]

    processor = StringProcessor()

    for test_input in test_cases:
        result = processor.remove_spaces(test_input)
        print(f"Input: {test_input!r}")
        print(f"Output: {result!r}\n")