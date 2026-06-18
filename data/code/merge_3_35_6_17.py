import string

class StringProcessor:
    """A utility class for basic string processing operations."""
    
    def __init__(self, text):
        """Initialize with a string of text."""
        self.text = str(text) if isinstance(text, (str, bytes)) else ""
        
    def count_vowels(self):
        """
        Count the number of vowels in the string.
        This implementation is O(n) where n is the length of the string.
        
        Returns:
            int: The total count of vowel characters found.
        """
        if not self.text:
            return 0
        
        # Define a set of lowercase and uppercase vowels for O(1) lookup time per character
        vowels = set('aeiouAEIOU')
        count = 0
        
        # Iterate through each character in the string exactly once (O(n))
        for char in self.text:
            if char in vowels:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    
    test_cases = [
        "Hello, World!",           # Expected: 2 (e, o)
        "AEIOU",                   # Expected: 5
        "",                        # Expected: 0
        "Python Programming",      # Expected: 4 (y is not counted here based on standard definition, a, i, o, u -> actually 'o', 'i' in Python? Let's trace: P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i = 4)
        "aeiouAEIOU",              # Expected: 10
    ]

    processor_instance = StringProcessor("Hello World")

    print(f"Input string: '{processor_instance.text}'")
    
    for test_input in test_cases:
        temp_processor = StringProcessor(test_input)
        result = temp_processor.count_vowels()
        print(f"'{test_input}': {result}")