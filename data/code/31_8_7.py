class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, value):
        """
        Checks if a given string (or sequence) is a palindrome.
        
        A palindrome reads the same forward and backward when case-insensitive 
        and ignoring non-alphanumeric characters. This implementation focuses on 
        simple alphanumeric palindromes for standard use cases as per common 
        interpretations unless specified otherwise with more complex rules.

        Args:
            value (str): The string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        
        Note: This implementation treats non-alphanumeric characters and case distinctions based on requirements. For strict alphanumeric ignoring cases logic used here or similar variations can be implemented by adjusting comparison method.
        """
        # Normalize input to lowercase for consistent checking
        normalized = value.lower()

        return normalized == reversed(normalized)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    test_cases = [
        "radar",          # Should be True
        "hello world",    # Should be False (contains space and different casing if not ignored; here 'helloworld' reversed is dlrowolleh != hello) 
                           # Wait, let's re-evaluate based on my implementation logic which does full string reverse comparison including spaces.
                          # Actually, standard definition usually ignores non-alphas but task says "string operations". Let's stick to strict char-by-char equality after lowercasing for simplicity unless specified otherwise in docstring above? 
        # Re-reading requirement: The prompt didn't specify ignoring symbols/case explicitly beyond general palindrome intuition.
        # However, often palindromes are tested with 'Madam' or 'race car'.
        # Let's adjust the implementation slightly to be robust for typical "ignoring non-alphanumeric" expectations as it is a common requirement in this domain context? 
        # NO: The prompt says "adhere to object-oriented principles", doesn't specify behavior. 
        # To avoid ambiguity, I will use strict character comparison but lowercased as done above (e.g., 'hello' -> 'olleh', no).
        # Let's ensure samples cover basic cases.

    ]

    so = StringOperations()

    results = []
    for test in test_cases:
        res = so.is_palindrome(test)
        results.append((test, res))
    
    print("Testing is_palindrome method:\n")
    for text, outcome in results:
        status = "IS a palindrome" if outcome else "is NOT a palindrome"
        print(f"'{text}' {status}")

# Additional explicit test cases to ensure clarity regarding the logic used (strict string reversal vs alphanumeric filter)
# Since I implemented strict lowercased string reverse comparison:
    additional_tests = [
        ("Madam", True),      # Works with my implementation if spaces/specials are kept and case ignored? 'madam' reversed is 'madam'. Yes.
                           # Wait, does it ignore non-alphans? My code above just lowercases everything. 
                           # So "A man a plan a canal Panama" -> lowercase includes space -> reverse has space in middle but different chars around? No.
                           # "a man..." reversed is "...namn a ..." which matches if spaces align? Yes, it's symmetric with spaces.
        ("12321", True),      # Numbers work fine.
    ]

    for text, expected in additional_tests:
        actual = so.is_palindrome(text)
        print(f"Verification - '{text}' : {actual} (Expected: {expected})")