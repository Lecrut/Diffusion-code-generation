class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text)
    
    def count_vowels(self):
        """Calculate and return the total vowel count in the text (case-insensitive)."""
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test sentence with AEIOU and OaEiO."
    counter = VowelCounter(sample_text)
    result = counter.count_vowels()
    print(f"Total vowel count: {result}")