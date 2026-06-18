class StringProcessor:
    """A class to process strings with various utility methods."""

    def count_vowels(self, text: str) -> int:
        """
        Counts the number of vowels in the given string.
        
        This implementation is O(n) where n is the length of the input string.
        It iterates through each character once and checks if it's a vowel (case-insensitive).

        Args:
            text (str): The input string to count vowels from.

        Returns:
            int: The total number of vowels found in the string.
        """
        # Define set of lowercase vowels for O(1) lookup time during iteration
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        vowel_count = 0
        
        # Iterate through each character exactly once -> O(n)
        for char in text:
            if char.lower() in vowels:
                vowel_count += 1
                
        return vowel_count

if __name__ == '__main__':
    # Hard-coded sample values to test the implementation without user input or external dependencies
    
    processor = StringProcessor()
    
    # Test case 1: Simple sentence with multiple vowels
    sample_1 = "Hello, World!"
    result_1 = processor.count_vowels(sample_1)
    print(f"Sample 'Hello, World!' - Vowel count: {result_1}")

    # Test case 2: String with no vowels (consonants and symbols only)
    sample_2 = "Brrr!!!"
    result_2 = processor.count_vowels(sample_2)
    print(f"Sample 'Brrr!!!' - Vowel count: {result_2}")

    # Test case 3: Mixed cases including uppercase vowels and numbers
    sample_3 = "AEIOU1234567890"
    result_3 = processor.count_vowels(sample_3)
    print(f"Sample 'AEIOU123...' - Vowel count: {result_3}")

    # Test case 4: Empty string
    sample_4 = ""
    result_4 = processor.count_vowels(sample_4)
    print(f"Sample '' (empty) - Vowel count: {result_4}")