class VowelCounter:
    def __init__(self, text: str):
        """Initialize with a string."""
        self.text = text
    
    def count_vowels(self) -> int:
        """Calculate and return the total vowel count in the text.
        
        Considers both uppercase and lowercase vowels (a, e, i, o, u)."""
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_strings = [
        "Hello, World!",
        "aeiouAEIOU",
        "",
        "Python Programming"
    ]

    for s in test_strings:
        counter = VowelCounter(s)
        count = counter.count_vowels()
        print(f"'{s}' has {count} vowels.")