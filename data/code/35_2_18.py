class VowelCounter:
    def __init__(self, text: str):
        """Initialize with a string."""
        self.text = text.lower() if isinstance(text, str) else ""
    
    def count_vowels(self) -> int:
        """Calculate and return the total vowel count in the input string."""
        vowels = set('aeiou')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "AEIOU",
        "Python Programming",
        ""
    ]

    for test_str in sample_strings:
        counter = VowelCounter(test_str)
        print(f"Input: '{test_str}' -> Total vowels: {counter.count_vowels()}")