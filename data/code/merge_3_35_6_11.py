class StringProcessor:
    """A utility class for basic string processing operations."""

    def count_vowels(self, text: str) -> int:
        """
        Count the number of vowels in the given text.
        
        This method is case-insensitive and considers 'a', 'e', 'i', 'o', 'u' as vowels.
        It iterates through each character once to ensure O(n) time complexity, where n is the length of the string.

        Args:
            text (str): The input string to process.

        Returns:
            int: The count of vowel characters in the string.
        """
        vowels = set("aeiouAEIOU")
        count = 0
        
        # Iterate through each character exactly once for O(n) complexity
        for char in text:
            if char in vowels:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    processor = StringProcessor()

    test_cases = [
        "Hello, World!",      # Expected: 2 (e, o)
        "AEIOU",              # Expected: 5
        "Programming is fun.",# Expected: 4 (o, a, i, u - case insensitive check needed in logic but set handles it) -> actually 'o','r'!='vowel', 'a','i','u'. Let's re-eval: P-r-o-g-r-a-m-m-i-n-g-_-i-s-_-f-u-n-. Vowels: o, a, i, i, u. Count = 5.
        "12345",              # Expected: 0
        "",                   # Expected: 0
    ]

    for test_string in test_cases:
        result = processor.count_vowels(test_string)
        print(f"Input: '{test_string}' -> Vowel Count: {result}")