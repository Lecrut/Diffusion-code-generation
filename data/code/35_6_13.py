class StringProcessor:
    def count_vowels(self, text):
        """
        Counts the number of vowels in a given string (a, e, i, o, u).
        Case-insensitive and O(n) time complexity where n is the length of the string.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            int: The count of vowels in the string.
        """
        if not isinstance(text, str):
            return 0
            
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        
        for char in text.lower():
            if char in vowel_set:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    samples = [
        "Hello, World!",
        "AEIOUaeiou",
        "",
        "Python programming is fun.",
        "No vowels here!"
    ]

    processor = StringProcessor()

    for sample in samples:
        result = processor.count_vowels(sample)
        print(f"Input: '{sample}'")
        print(f"Vowel count: {result}\n")