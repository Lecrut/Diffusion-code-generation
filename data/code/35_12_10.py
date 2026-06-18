class VowelCounter:
    """A class to count vowels in a given text string."""
    
    def __init__(self):
        self.vowels = set("aeiouAEIOU")
        
    def count(self, text):
        """Returns the number of vowel characters present in the input string.

        Args:
            text (str): The string to analyze for vowels.

        Returns:
            int: The total count of vowel characters found.
        """
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    
    # Sample 1: Standard vowels only
    sample_1 = "Hello, World!"
    result_1 = counter.count(sample_1)
    
    # Sample 2: Mixed case and special characters
    sample_2 = "Python is awesome. The sky is blue."
    result_2 = counter.count(sample_2)
    
    # Sample 3: Empty string
    sample_3 = ""
    result_3 = counter.count(sample_3)

    print(f"Vowels in '{sample_1}': {result_1}")
    print(f"Vowels in '{sample_2}': {result_2}")
    print(f"Vowels in '{sample_3}': {result_3}")