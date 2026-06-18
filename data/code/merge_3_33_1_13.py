class StringProcessor:
    """A class to process strings with optimized operations."""
    
    def remove_spaces(self, input_string):
        """
        Removes all spaces from the given string in O(n) time complexity.
        
        Args:
            input_string (str): The input string containing potential spaces.
            
        Returns:
            str: A new string with all spaces removed.
        """
        # Using list comprehension for efficiency and built-in join is optimal in Python
        return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    test_cases = [
        "Hello World",
        "  Multiple   Spaces  ",
        "NoSpacesHere",
        "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    ]

    processor = StringProcessor()

    for test_input in test_cases:
        result = processor.remove_spaces(test_input)
        print(f'Input: "{test_input}"')
        print(f'Result: "{result}"\n')