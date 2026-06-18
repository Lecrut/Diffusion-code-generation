class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self, text):
        """Initialize with a string of text."""
        self.text = str(text)
        
    def get_vowel_count(self):
        """Calculate and return the total number of vowels (a, e, i, o, u) in the text.
        
        Returns:
            int: The count of vowel characters found in the string.
        """
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "",
        "AEIOUaeiou",
        "xyz"
    ]

    for sample in samples:
        counter = VowelCounter(sample)
        count = counter.get_vowel_count()
        print(f"'{sample}' -> {count} vowels")