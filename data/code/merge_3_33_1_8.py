class StringProcessor:
    """A class to process strings with optimized operations."""

    def remove_spaces(self, input_string):
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            input_string (str): The string to process.
            
        Returns:
            str: A new string with all spaces removed.
        """
        # Using list comprehension for efficiency and readability, 
        # which operates linearly relative to the length of the string.
        return ''.join(char for char in input_string if not ' '.__contains__(char) or char != ' ')

if __name__ == '__main__':
    processor = StringProcessor()

    test_cases = [
        "Hello World",
        "  Multiple   Spaces  ",
        "NoSpacesHere",
        "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    ]

    for test_input in test_cases:
        result = processor.remove_spaces(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")