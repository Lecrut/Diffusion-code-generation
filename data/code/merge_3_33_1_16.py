class StringProcessor:
    def remove_spaces(self, text):
        """
        Removes all spaces from an input string in O(n) time complexity.
        
        Args:
            text (str): The input string to process
            
        Returns:
            str: A new string with all spaces removed
        """
        result = []
        for char in text:
            if not char.isspace():
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    processor = StringProcessor()
    
    # Sample test cases - no user input required
    sample_inputs = [
        "Hello World",
        "Python   Programming  ",
        "NoSpacesHere",
        "Multiple   Spaces   Between Words",
        "",
        "OnlySpaced"
    ]
    
    for inp in sample_inputs:
        output = processor.remove_spaces(inp)
        print(f'Input: "{inp}" -> Output: "{output}"')