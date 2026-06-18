import string

class StringProcessor:
    def count_vowels(self, text):
        """
        Counts the number of vowels in a given string.
        
        Time Complexity: O(n) where n is the length of the input string.
        Space Complexity: O(1).
        
        Parameters:
            text (str): The input string to process.
            
        Returns:
            int: The count of vowel characters found in the string.
        """
        vowels = set("aeiouAEIOU")
        return sum(char in vowels for char in text)

if __name__ == "__main__":
    # Hard-coded sample values to ensure no user input or external dependencies are required
    processor = StringProcessor()

    test_cases = [
        "Hello, World!",          # Expected: 2 (e, o)
        "AEIOU",                   # Expected: 5
        "",                        # Expected: 0
        "Python Programming!",     # Expected: 4 (y is not counted here based on standard definition unless specified otherwise. 
                                   # Note: 'y' is sometimes considered a vowel but strictly it's consonant in this context without special instruction.)
                                   # Let's stick to strict A, E, I, O, U and their uppercase counterparts for simplicity and correctness as per standard definitions unless extended.
                                   # Actually, let's count 'y' here too just in case? No, task says vowels usually implies a,e,i,o,u. 
                                   # Re-evaluating "Python": P-y-t-h-o-n -> o is vowel (1). Wait, also y? 
                                   # Let's stick to A,E,I,O,U only for this strict implementation unless told otherwise.
                                   # Correction: In many contexts 'y' is a semi-vowel but standard programming tasks usually imply {a,e,i,o,u}.
                                   # I will implement strictly {a,e,i,o,u} + uppercase.
                                   
        "aeiouAEIOU",             # Expected: 10
    ]

    for test_string in test_cases:
        count = processor.count_vowels(test_string)
        print(f"Input: '{test_string}' -> Count of vowels: {count}")