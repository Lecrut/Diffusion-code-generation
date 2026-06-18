import sys

class StringUtils:
    """A utility class containing string manipulation methods."""

    def is_palindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        This method uses the two-pointer approach to compare characters from both ends
        moving towards the center without creating new strings or lists, ensuring O(n) time complexity
        and O(1) space complexity relative to the input size (excluding storage for the string itself).

        Parameters:
            s (str): The input string to check. Spaces are preserved in comparison as per standard palindrome logic
                     unless specified otherwise; here we compare all characters exactly. If case-insensitivity is 
                     desired, it should be handled before this function or via a wrapper method if needed. Currently,
                     it performs exact character matching including spaces and casing.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        
        Examples (internal):
            "radar" -> True
            "hello" -> False
        """
        left = 0
        right = len(s) - 1
        
        # Use two pointers to compare characters from start and end moving inward
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    test_cases = [
        "radar",           # Should be True
        "hello",           # Should be False
        "",               # Empty string is technically palindrome -> True
        "A man a plan a canal Panama",  # Note: This will return False because of case/space sensitivity unless preprocessed. 
                          # To make it work as expected in many contexts, one might preprocess to lowercase and remove non-alphanumeric.
                          # However, per strict instructions here without extra preprocessing logic requested explicitly for this function:
        "racecar",         # Should be True
    ]

    print("Running StringUtils.is_palindrome tests...")
    
    result = [test_case is not None]  # Placeholder to avoid printing immediately if empty list
    
    for test in test_cases:
        output = StringUtils().is_palindrome(test)
        expected_output = f"Expected {output} for '{test}'."

        print(output)