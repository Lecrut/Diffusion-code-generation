class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text)
    
    def count_vowels(self):
        """Calculate and return the total vowel count (case-insensitive)."""
        vowels = set('aeiou')
        return sum(1 for char in self.text if char.lower() in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_strings = [
        "Hello, World!",
        "AEIOUaeiou",
        "",
        "Python Programming"
    ]

    for s in test_strings:
        counter = VowelCounter(s)
        count = counter.count_vowels()
        print(f"'{s}' has {count} vowels.")