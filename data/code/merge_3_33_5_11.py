class TextProcessor:
    """A class to perform basic text cleaning operations."""
    
    def clean_text(self, text):
        """
        Removes all whitespace characters from the input string.
        
        This method handles spaces, tabs, newlines, and other Unicode 
        whitespace characters defined by Python's str.isalnum() logic complement.
        
        Args:
            text (str): The input string to clean.
            
        Returns:
            str: A new string with all whitespace removed.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Remove all Unicode whitespace characters using the translate method
        # or regex for explicit control over specific categories like \s which 
        # covers [ \t\n\r\f\v] plus other unicode whitespaces.
        return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or files are needed
    
    processor = TextProcessor()
    
    samples = [
        "Hello World",
        "\tNew Line\r\nHere",
        "   Multiple   Spaces   ",
        "NoSpacesAtAll"
    ]
    
    for sample in samples:
        cleaned_result = processor.clean_text(sample)
        print(f"Original: {repr(sample)}")
        print(f"Cleaned:  {repr(cleaned_result)}")
        print("-" * 20)