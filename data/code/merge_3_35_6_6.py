import string

class StringProcessor:
    """A utility class for basic string processing operations."""

    def count_vowels(self, text: str) -> int:
        """
        Counts the number of vowels in the given input string.
        
        This method is case-insensitive and considers 'a', 'e', 'i', 'o', 'u' as vowels.
        It operates with O(n) time complexity where n is the length of the text,
        by iterating through each character exactly once without nested loops or 
        expensive string operations like repeated slicing.

        Args:
            text (str): The input string to analyze. Can contain any characters.

        Returns:
            int: The total count of vowel characters found in the text.
        
        Example:
            >>> processor = StringProcessor()
            >>> result = processor.count_vowels("Hello World")
            # 'e', 'o' -> 2 vowels (case insensitive)
            >>> print(result) 
            3
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string input, got {type(text).__name__}")

        count = 0
        
        # Define lowercase and uppercase vowel sets for efficient lookup
        vowels_lower = set("aeiou")
        vowels_upper = set("AEIOU")
        
        # Iterate through each character exactly once (O(n))
        for char in text:
            if char.lower() in vowels_lower or char.upper() in vowels_upper:
                count += 1
                
        return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    processor = StringProcessor()
    
    test_cases = [
        "Hello World",           # Expected: 3 ('e', 'o', 'o')
        "AEIOUaeiou",            # Expected: 10 (all are vowels)
        "",                      # Expected: 0 (empty string)
        "Rhythm is sweet!",     # Expected: 2 ('y' usually not counted here based on strict aeiou, 'e', 'i') -> Actually 'e','i'. Wait. R-y-t-h-m-i-s-s-w-e-e-!. Vowels are e,i,e,e? No. i, e, e. Let's recheck: r,y,t,h,m,(no),i,s,s,w,(no),e,e,(no). So 3 vowels (i, e, e).
        "Python Programming",    # Expected: 4 ('o','y'?, 'r'? no, 'a', 'g'? no. P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i. Total 4.)
        "bcdfghjklmnpqrstvwxz", # Expected: 0 (no vowels)
    ]

    print("Running StringProcessor count_vowels tests...\n")
    
    for test_input in test_cases:
        result = processor.count_vowels(test_input)
        print(f"Input: '{test_input}' -> Vowel Count: {result}")