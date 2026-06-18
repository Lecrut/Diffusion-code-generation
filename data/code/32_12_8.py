class StringAnalyzer:
    def get_length(self, text):
        """
        Calculates and returns the length of the input string.
        
        Args:
            text (str): The string to analyze.
            
        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Sample test cases running without user input or command-line arguments
    analyzer = StringAnalyzer()
    
    samples = [
        "Hello, World!",
        "",
        "Python is great.",
        "a",
        "12345"
    ]
    
    for sample in samples:
        length = analyzer.get_length(sample)
        print(f"String: '{sample}' -> Length: {length}")