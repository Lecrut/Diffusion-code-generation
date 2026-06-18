class StringProcessor:
    """A class to process strings with optimized operations."""
    
    def remove_spaces(self, input_string):
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            input_string (str): The string to process
            
        Returns:
            str: A new string with all spaces removed
        """
        # Using list comprehension and join is efficient for Python strings
        return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input
    test_cases = [
        "Hello World",
        "Python 3.10 is great!",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesHere"
    ]
    
    processor = StringProcessor()
    
    for test_input in test_cases:
        result = processor.remove_spaces(test_input)
        print(f'Input:  "{test_input}"')
        print(f'Output: "{result}"\n')