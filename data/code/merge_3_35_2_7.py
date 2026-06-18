class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text)
    
    def count_vowels(self):
        """Calculate and return the total vowel count (case-insensitive)."""
        vowels = set('aeiouAEIOU')
        count = sum(1 for char in self.text if char in vowels)
        return count

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "The quick brown fox jumps over the lazy dog",
        "Aeiou AEIOU"
    ]

    for test_string in sample_strings:
        counter = VowelCounter(test_string)
        result = counter.count_vowels()
        print(f"'{test_string}' has {result} vowels.")