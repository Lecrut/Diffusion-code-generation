import string

class StringProcessor:
    """A class designed to perform basic string processing operations."""
    
    def __init__(self, text):
        """Initialize with a string of text."""
        self.text = str(text)
        
    def count_vowels(self):
        """
        Counts the number of vowels in the string.
        
        This method iterates through each character in the string exactly once,
        checking if it is a vowel (a, e, i, o, u), regardless of case.
        The time complexity is O(n) where n is the length of the string.
        
        Returns:
            int: The count of vowels found in the text.
        """
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU123"
    ]

    processor = StringProcessor("The quick brown fox jumps over the lazy dog.")
    
    print(f"Vowel count in sample: {processor.count_vowels()}")
    
    # Testing with additional samples from the list
    for s in samples:
        sp = StringProcessor(s)
        vowel_count = sp.count_vowels()
        print(f"'{s}' -> Vowels: {vowel_count}")