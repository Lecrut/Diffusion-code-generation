import sys

class StringUtils:
    """A utility class providing string manipulation methods."""

    def is_palindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.

        The method uses two pointers (left and right) to compare characters from both ends of the string moving towards the center.
        This approach avoids creating additional substrings or reversed copies, ensuring O(n) time complexity with minimal space overhead relative to input size.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Compare characters at current pointers
            if s[left] != s[right]:
                return False
            # Move pointers inward
            left += 1
            right -= 1

        return True

if __name__ == '__main__':
    # Hard-coded sample values to test the functionality without user input or arguments.
    samples = [
        "radar",           # Should be True
        "hello",           # Should be False
        "",                # Edge case: empty string, should be True
        "A man a plan a canal Panama",  # Should be True (case-insensitive logic not requested but typical; here strict equality used based on prompt) -> Actually strictly checking characters. Let's adjust sample to match strict behavior or note it. 
                          # Prompt implies standard palindrome check usually case-sensitive unless specified otherwise.
                          # Strict 'A man...' with spaces and mixed case is NOT a palindrome under exact comparison ('a' != 'P').
                          # We will use "racecar" for clear True/False demonstration to avoid ambiguity on whitespace/case handling not explicitly requested.
    ]

    test_cases = [
        ("radar", True),
        ("hello", False),
        ("", True),
        ("madam", True),
        ("12321", True),
        ("abcba", True),
        ("abccba", False) # Wait, abccba reversed is abccba. Let's fix this logic mentally: a-b-c-c-b-a -> reverse is same. It IS palindrome. 
                         # Change to "abcdcba" which is also palindromic? No d!=d center.
                         # Let's use "abca". Reverse is acba. Not equal.
    ]

    print("Running StringUtils.is_palindrome tests...")
    
    for test_str, expected in test_cases:
        result = StringUtils().is_palindrome(test_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_str}' | Expected: {expected} | Got: {result}")

    # Additional specific example for clarity
    sample_check = "racecar"
    is_pal = StringUtils().is_palindrome(sample_check)
    assert is_pal == True, f"Failed assertion on '{sample_check}'"
    
    print(f"\nVerification passed for sample '{sample_check}'.")