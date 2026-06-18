class StringProcessor:
    """A utility class for basic string processing operations."""

    def count_vowels(self, text: str) -> int:
        """
        Counts the total number of vowels in the given string.
        
        This implementation iterates through the string once to ensure O(n) time complexity.
        It considers both uppercase and lowercase vowels ('a', 'e', 'i', 'o', 'u').

        Args:
            text (str): The input string to process.

        Returns:
            int: The count of vowel characters in the text.
        """
        if not isinstance(text, str):
            return 0
        
        vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        count = 0

        for char in text:
            # Check if the character is a vowel using O(1) dictionary lookup
            if char.lower() in vowels:
                count += 1
        
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is required
    
    test_cases = [
        "Hello, World!",      # Expected: 2 (e, o) - Wait, 'o' in world? H-e-l-l-o W-o-r-l-d. e,o -> 2. Actually O and E are vowels. 
                             # Correction: Hello (H,e,l,l,o), World (W,o,r,l,d). Vowels: e, o, o. Total = 3.
        "AEIOU",              # Expected: 5
        "",                   # Expected: 0
        "Python Programming!",# P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g-. O,o,a,i -> 4
    ]

    processor = StringProcessor()

    print("Testing vowel counting functionality:\n")

    for i, test_string in enumerate(test_cases):
        count = processor.count_vowels(test_string)
        # Manual verification of expected results based on the logic:
        # "Hello, World!" -> e, o, o => 3
        if isinstance(test_string, str):
            print(f"Input: {test_string!r}")
            print(f"Vowel Count: {count}\n")