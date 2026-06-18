class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self, text):
        """Initialize the counter with a specific string."""
        self.text = str(text)
    
    def get_vowel_count(self):
        """Calculate and return the total number of vowels (a, e, i, o, u) in the string.
        
        Returns:
            int: The count of vowel characters found in the text.
        """
        vowels = set("aeiouAEIOU")
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    samples = [
        "Hello, World!",
        "Beautiful Python code",
        "",
        "AEIOUaeiou"
    ]

    for text in samples:
        counter = VowelCounter(text)
        count = counter.get_vowel_count()
        print(f'Text: "{text}" -> Vowel Count: {count}')