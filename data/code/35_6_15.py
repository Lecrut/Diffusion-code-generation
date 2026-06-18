class StringProcessor:
    """A class to perform various string processing operations."""

    def count_vowels(self, text: str) -> int:
        """
        Count the number of vowels in the given text.
        
        This implementation runs in O(n) time complexity where n is the length of the input string.
        It considers both uppercase and lowercase vowels (a, e, i, o, u).

        Args:
            text (str): The input string to process.

        Returns:
            int: The count of vowels found in the string.
        """
        vowel_set = {'aeiouAEIOU'}
        count = 0
        
        for char in text:
            if char in vowel_set:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "Hello World",
        "AEIOUaeiou",
        "Python Programming Language",
        "",
        "xyz"
    ]

    processor = StringProcessor()

    for text in test_cases:
        vowel_count = processor.count_vowels(text)
        print(f'Text: "{text}" -> Vowel count: {vowel_count}')