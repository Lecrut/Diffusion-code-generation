class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = text
    
    def count_vowels(self):
        """Calculate and return the total vowel count in the text."""
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test sentence with AEIOU and aeiou."
    counter = VowelCounter(sample_text)
    vowel_count = counter.count_vowels()
    print(f"Total vowel count: {vowel_count}")