class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = text
    
    def count_vowels(self) -> int:
        """Calculate and return the total vowel count in the text (case-insensitive)."""
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    samples = [
        "Hello World!",
        "Python is amazing.",
        "",
        "AEIOU"
    ]
    
    for text in samples:
        counter = VowelCounter(text)
        print(f"'{text}' has {counter.count_vowels()} vowels.")