class StringAnalyzer:
    def get_length(self, text):
        """
        Computes and returns the length of the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    samples = [
        "Hello, World!",
        "",
        "Python 3.9",
        "12345"
    ]
    
    for sample in samples:
        length = analyzer.get_length(sample)
        print(f"'{sample}' has a length of {length}.")