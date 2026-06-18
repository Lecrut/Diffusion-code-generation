class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text)

    def count_vowels(self):
        """Calculate and return the total vowel count (case-insensitive)."""
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "",
        "AEIOUaeiou",
        "Rhythm"  # Contains 'y' but we only count aeiou by default unless specified otherwise. 
                # Based on standard definition: Rhythm has no vowels here (assuming strict a,e,i,o,u).
    ]

    for sample in samples:
        counter = VowelCounter(sample)
        total_count = counter.count_vowels()
        print(f"Text: '{sample}' -> Total vowel count: {total_count}")