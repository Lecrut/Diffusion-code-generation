class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self, text):
        """
        Initialize the VowelCounter with a string.
        
        Args:
            text (str): The input string to analyze for vowel counts.
        """
        self.text = str(text)

    def count_vowels(self):
        """
        Calculate and return the total number of vowels in the stored text.
        
        Returns:
            int: The count of vowels found in the text (case-insensitive).
        """
        vowels_set = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels_set)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello, World!",
        "Programming is awesome.",
        "",
        "AEIOU",
        "Python3"
    ]

    for sample in samples:
        counter = VowelCounter(sample)
        count = counter.count_vowels()
        print(f"Text: '{sample}' -> Vowel Count: {count}")