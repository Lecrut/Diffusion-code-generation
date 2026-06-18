class StringAnalyzer:
    def __init__(self):
        """Initialize a new instance of StringAnalyzer."""
        pass
    
    def get_length(self, text: str) -> int:
        """
        Computes and returns the length of the input string.
        
        Args:
            text (str): The input string for which the length is to be calculated.
            
        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    sample_texts = [
        "Hello, World!",
        "",
        "Python 3.12",
        "   Spaces around text   ",
        "Special chars: !@#$%^&*()"
    ]
    
    for i in range(len(sample_texts)):
        test_string = sample_texts[i]
        calculated_length = analyzer.get_length(test_string)
        
        print(f"Input {i+1}: '{test_string}'")
        print(f"Length: {calculated_length}")