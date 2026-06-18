class VowelCounter:
    """A class to count vowels in a given text string."""
    
    def __init__(self):
        self.vowels = set("aeiouAEIOU")
    
    def count(self, text: str) -> int:
        """Returns the number of vowel characters in the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            int: The total count of vowels found in the string.
        """
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    
    sample_text_1 = "Hello, World!"
    sample_text_2 = "AEIOUaeiou"
    sample_text_3 = "Python programming is awesome."
    
    result_1 = counter.count(sample_text_1)
    result_2 = counter.count(sample_text_2)
    result_3 = counter.count(sample_text_3)
    
    print(f"Vowel count in '{sample_text_1}': {result_1}")
    print(f"Vowel count in '{sample_text_2}': {result_2}")
    print(f"Vowel count in '{sample_text_3}': {result_3}")