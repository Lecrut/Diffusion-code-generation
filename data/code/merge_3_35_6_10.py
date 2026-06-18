class StringProcessor:
    """A class to perform various string processing operations."""
    
    def count_vowels(self, text: str) -> int:
        """
        Counts the number of vowels in the given string.
        
        This implementation is O(n) where n is the length of the input string,
        as it iterates through each character exactly once.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            int: The count of vowels found in the string.
            
        Vowels considered include 'a', 'e', 'i', 'o', 'u' and their uppercase equivalents.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        vowel_count = 0
        vowels = set('aeiouAEIOU')
        
        for char in text:
            if char in vowels:
                vowel_count += 1
                
        return vowel_count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    processor = StringProcessor()
    
    test_cases = [
        "hello world",      # Expected: 2 (e, o)
        "AEIOU",            # Expected: 5
        "rhythm",           # Expected: 0
        "aeiouaeiou",       # Expected: 10
        "",                 # Expected: 0
    ]
    
    for test_string in test_cases:
        count = processor.count_vowels(test_string)
        print(f"Text: '{test_string}' -> Vowel Count: {count}")