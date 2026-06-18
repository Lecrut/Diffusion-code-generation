class StringProcessor:
    def count_vowels(self, text: str) -> int:
        """
        Counts the number of vowels in a given string.
        
        This method is case-insensitive and considers 'a', 'e', 'i', 'o', 'u' as vowels.
        It iterates through each character once, ensuring O(n) time complexity where n is 
        the length of the input string.

        Args:
            text (str): The input string to process.

        Returns:
            int: The count of vowel characters in the string.
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_strings = [
        "Hello, World!",
        "AEIOUaeiou",
        "",
        "rhythm",
        "Python programming"
    ]

    processor = StringProcessor()

    for test_str in test_strings:
        count = processor.count_vowels(test_str)
        print(f'String: "{test_str}" -> Vowel Count: {count}')