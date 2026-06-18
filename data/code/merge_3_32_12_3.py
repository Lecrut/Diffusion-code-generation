class StringAnalyzer:
    """A class designed to analyze string properties."""
    
    def get_length(self, text):
        """Calculates and returns the length of the input string.
        
        Args:
            text (str): The string for which the length needs to be calculated.
            
        Returns:
            int: The number of characters in the provided string.
        """
        return len(text)

if __name__ == '__main__':
    sample_text_1 = "Hello, World!"
    sample_text_2 = ""
    
    analyzer = StringAnalyzer()
    
    result_1 = analyzer.get_length(sample_text_1)
    print(f"Length of '{sample_text_1}': {result_1}")
    
    result_2 = analyzer.get_length(sample_text_2)
    print(f"Length of '{sample_text_2}': {result_2}")