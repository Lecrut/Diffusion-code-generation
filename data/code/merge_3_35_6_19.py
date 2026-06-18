import string

class StringProcessor:
    """A class designed to perform basic string processing tasks."""
    
    def __init__(self, text):
        self.text = str(text) if not isinstance(text, str) else text
    
    def count_vowels(self):
        """
        Counts the number of vowels in the string.
        
        This implementation iterates through each character exactly once,
        ensuring an O(n) time complexity where n is the length of the string.
        
        Returns:
            int: The total count of vowel characters (a, e, i, o, u - case insensitive).
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

    processor = StringProcessor("Sample text with vowels: a e i o u")
    
    print(f"Input string length: {len(processor.text)}")
    print(f"Vowel count in sample: {processor.count_vowels()}")
    
    # Demonstrate the method on other samples directly for verification
    test_cases = [
        ("Hello, World!", 2),   # e, o
        ("aeiouAEIOU", 10)      # all are vowels
    ]

    print("\nVerification of specific cases:")
    for text, expected_count in test_cases:
        p = StringProcessor(text)
        result = p.count_vowels()
        status = "PASS" if result == expected_count else "FAIL"
        print(f"Text: '{text}' -> Count: {result} (Expected: {expected_count}) [{status}]")