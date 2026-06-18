class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self, text):
        """Initialize with a string of text."""
        self.text = str(text)
        
    def get_vowel_count(self):
        """Calculate and return the total number of vowels (a, e, i, o, u) 
        in uppercase or lowercase.
        
        Returns:
            int: The count of vowels found in the text.
        """
        vowels = set('aeiouAEIOU')
        count = 0
        
        for char in self.text:
            if char in vowels:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    
    test_cases = [
        "Hello World",
        "aeiouAEIOU",
        "Python Programming",
        ""  # Edge case: empty string
    ]

    for text in test_cases:
        counter = VowelCounter(text)
        count = counter.get_vowel_count()
        print(f"Text: '{text}' -> Vowel Count: {count}")