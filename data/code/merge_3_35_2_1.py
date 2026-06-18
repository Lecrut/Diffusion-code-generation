class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text) if isinstance(text, (str)) else ""

    def count_vowels(self):
        """Calculate and return the total vowel count in the text.
        
        Vowels are defined as 'a', 'e', 'i', 'o', 'u' (case-insensitive).
        Returns an integer representing the count of vowels found.
        """
        if not self.text:
            return 0
        
        vowels = set("aeiouAEIOU")
        count = sum(1 for char in self.text if char in vowels)
        
        return count

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "Hello World",
        "aeiouAEIOU",
        "",
        "Python Programming",
        "The quick brown fox jumps over the lazy dog"
    ]

    for test_string in test_cases:
        counter = VowelCounter(test_string)
        result = counter.count_vowels()
        print(f"'{test_string}' -> {result} vowels")