import string

class StringProcessor:
    """A utility class for basic string processing operations."""
    
    def __init__(self, text: str = ""):
        self.text = text
    
    def count_vowels(self) -> int:
        """
        Counts the number of vowels in the current string.
        
        This implementation iterates through each character exactly once,
        ensuring O(n) time complexity where n is the length of the string.
        
        Returns:
            int: The total count of vowel characters (a, e, i, o, u, case-insensitive).
        """
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Hello, World!",
        "aeiouAEIOU",
        "",
        "Python Programming 101"
    ]

    processor = StringProcessor()

    for test_string in samples:
        # Initialize the processor with each sample string to demonstrate independence per run if needed.
        temp_processor = StringProcessor(test_string)
        count = temp_processor.count_vowels()
        print(f"'{test_string}' -> Vowel Count: {count}")