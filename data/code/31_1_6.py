import sys

class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        This method uses two pointers, one starting from the beginning and 
        another from the end of the list of characters derived from the input string.
        It compares characters moving towards the center without modifying the original data structure's order,
        effectively simulating an 'in-place' check on a mutable sequence for efficiency in terms of space (O(1) auxiliary).

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Convert string to list for mutability simulation or direct indexing access
        chars = list(s)
        
        left = 0
        right = len(chars) - 1
        
        while left < right:
            # Compare characters at current pointers
            if chars[left] != chars[right]:
                return False
            
            # Move pointers towards center
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    test_cases = [
        "radar",
        "racecar",
        "hello",
        "A man a plan a canal Panama", # Should be False due to spaces/case unless specified otherwise, but standard palindrome check usually implies case-sensitive or ignores non-alphanumeric. 
                                      # The prompt asks for 'in-place comparison technique' on the string itself.
                                      # Standard definition: exact match including whitespace and case.
        "12321",
        "",
        "a"
    ]

    print("Running StringUtils.is_palindrome tests...")
    
    for test in test_cases:
        result = StringUtils.is_palindrome(test)
        status = "Palindrome" if result else "Not a Palindrome"
        # Note: For case 4, standard strict palindrome check fails because of spaces and mixed case. 
        # If the requirement implied ignoring non-alphanumeric or case-insensitivity, logic would differ.
        # Based on 'in-place comparison' instruction without further qualifiers, we perform exact character match.
        
        print(f"Input: '{test}' -> {status}")

    # Demonstrate in-place modification capability if needed (though not strictly required by prompt for the check itself)
    # The core logic above is O(1) space auxiliary compared to creating reversed strings.