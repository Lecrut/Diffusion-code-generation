class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self):
        self.vowels = set("aeiouAEIOU")
        
    def count(self, text):
        """Counts the number of vowels in the input string.
        
        Args:
            text (str): The string to analyze for vowel occurrences.
            
        Returns:
            int: The total count of vowels found in the string.
        """
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    
    # Sample test cases with hard-coded values
    sample_texts = [
        "Hello, World!",
        "AEIOU",
        "",
        "Python Programming 101",
        "aeiou AEIOU"
    ]
    
    for text in sample_texts:
        count = counter.count(text)
        print(f"'{text}' contains {count} vowel(s).")