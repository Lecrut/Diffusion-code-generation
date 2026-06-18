class StringCleaner:
    def clean(self, text):
        """
        Removes all spaces from the input string efficiently.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with all spaces removed.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Using list comprehension and join is generally efficient for strings in Python
        return ''.join(char for char in text if char != ' ')

if __name__ == '__main__':
    cleaner = StringCleaner()
    
    sample_inputs = [
        "Hello World",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesAtAll",
        "Mixed: spaces, tabs,\nand newlines"  # Note: only ' ' (space) is removed per spec
    ]
    
    for test_input in sample_inputs:
        result = cleaner.clean(test_input)
        print(f"Input:    {repr(test_input)}")
        print(f"Output:   {repr(result)}")
        print("-" * 30)