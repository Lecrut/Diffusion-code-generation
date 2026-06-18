class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text)

    def count_vowels(self):
        """Calculate and return the total vowel count in the initialized string.
        
        Considers both uppercase and lowercase vowels (a, e, i, o, u).
        Returns an integer representing the count of vowels found anywhere 
        within the text sequence.
        """
        vowels = set("aeiouAEIOU")
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    test_cases = [
        "Hello World",
        "AEIOUaeiou",
        "",
        "Python Programming"
    ]

    for text in test_cases:
        counter = VowelCounter(text)
        count = counter.count_vowels()
        print(f"'{text}' has {count} vowel(s).")