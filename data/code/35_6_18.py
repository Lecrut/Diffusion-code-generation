import string

class StringProcessor:
    """A class to perform various operations on strings."""

    def count_vowels(self, text: str) -> int:
        """Count the number of vowels in a given string.

        This method is implemented with O(n) time complexity where n is 
        the length of the input string. It iterates through each character 
        once and checks if it is a vowel (case-insensitive).

        Args:
            text (str): The input string to analyze.

        Returns:
            int: The count of vowels in the string.
        
        Time Complexity: O(n) - Single pass through the string.
        Space Complexity: O(1) - Only a few variables are used regardless of input size.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        vowels = set(string.ascii_letters.split('')) # Initialize set with all letters to avoid repeated check or simple list lookup
        
        vowel_count = 0
        
        for char in text:
            lowercase_char = char.lower()
            
            if lowercase_char == 'a' or \
               lowercase_char == 'e' or \
               lowercase_char == 'i' or \
               lowercase_char == 'o' or \
               lowercase_char == 'u':
                vowel_count += 1
                
        return vowel_count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    
    test_cases = [
        ("Hello World", 2),          # e, o
        ("Python Programming", 4),   # y? usually not counted here unless specified. Standard vowels: P-y-t-h-o-n... wait python has 'o'. progra-m-ming. p-r-o-g-r-a-m-i-n-g. o, a, i. total 3 in programming + o in pytho = 4
        ("AEIOUaeiou", 10),          # all letters present exactly once each case
        ("Rhythm is easy.", 2),      # only 'i' and 'e'? no: y-h-t-m-rh-y-s-i-e-a-. vowels are i, e. yes. Wait 'y' is not standard vowel in this logic unless added. Logic uses a,e,i,o,u.
        ("", 0)                      # empty string
    ]

    processor = StringProcessor()

    print("String Processor Vowel Counting Results\n")
    
    for i, (input_str, expected_count) in enumerate(test_cases, 1):
        result = processor.count_vowels(input_str)
        
        status = "PASS" if result == expected_count else f"FAIL (Expected {expected_count}, Got {result})"
        print(f"Test Case {i}:")
        print(f"Input: '{input_str}'")
        print(f"Vowel Count: {result} - Status: [{status}]")
        
    # Additional specific test for 'y' exclusion to clarify standard definition used here
    special_case = "Why do we say yes?" 
    result_special = processor.count_vowels(special_case)
    
    print("\nSpecial Case (Testing that 'y' is NOT counted based on a,e,i,o,u logic):")
    print(f"Input: '{special_case}'")
    print(f"Vowel Count: {result_special}")