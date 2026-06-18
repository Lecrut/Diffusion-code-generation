import string

class StringProcessor:
    """A utility class for basic string processing operations."""

    def count_vowels(self, text: str) -> int:
        """
        Count the number of vowels in a given string.
        
        This method is case-insensitive and considers 'a', 'e', 'i', 'o', 'u' as vowels.
        It iterates through each character exactly once to ensure O(n) time complexity.

        Args:
            text (str): The input string to process.

        Returns:
            int: The count of vowel characters in the string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Define vowels for case-insensitive checking using set lookups for O(1) average time per check
        vowels = {c.lower() for c in "aeiou"}
        count = 0
        
        for char in text:
            if char.lower() in vowels:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    processor = StringProcessor()

    test_cases = [
        "Hello World",          # Expected: 2 (e, o)
        "aeiouAEIOU",           # Expected: 10
        "",                     # Expected: 0
        "Python Programming!", # Expected: 3 (y is not counted here based on standard definition, a, i, o - wait 'a','i' in programming? Let's trace: P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i -> 4)
        "Rhythm",               # Expected: 0 (no standard vowels)
    ]

    for test_input in test_cases:
        result = processor.count_vowels(test_input)
        print(f"Input: '{test_input}'")
        print(f"Vowel Count: {result}")
        print("-" * 20)