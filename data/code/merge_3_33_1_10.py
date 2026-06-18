class StringProcessor:
    def remove_spaces(self, s):
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            s (str): The input string containing potential whitespace characters.
            
        Returns:
            str: A new string with all space characters removed.
        """
        return ''.join(char for char in s if not char == ' ')

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
        print(f'Input:  "{test_input}"')
        print(f'Output: "{result}"\n')