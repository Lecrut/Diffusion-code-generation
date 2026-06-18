import sys

class StringUtils:
    def is_palindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        Since Python strings are immutable and cannot be modified in place efficiently 
        without creating new objects or converting to lists (which also involves copying),
        the "in-place" logic here refers to comparing characters from both ends moving 
        towards the center, avoiding full string reversal copies where possible by using 
        two pointers on indices. This is the most efficient approach for Python strings 
        as it runs in O(n) time and uses minimal extra space (O(1) auxiliary beyond input).
        
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
            
            # Move both pointers inward simultaneously (simulating in-place traversal logic)
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),  # Case-insensitive check not implemented per strict requirement unless specified; keeping case-sensitive for simplicity as no normalization requested. If case-insensitivity is needed, it should be explicitly stated in the task prompt which it isn't here. However, standard palindrome definition often implies ignoring spaces/case depending on context. Given "optimized" and "in-place", we stick to exact character match unless told otherwise. Let's adjust for common expectation: usually palindromes ignore non-alphanumeric or case. But without explicit instruction, strict equality is safer. Re-reading task: just says 'string'. We will implement strict comparison as per literal interpretation of input string.)
        ("", True),  # Empty string is a palindrome
        ("12321", True),
        ("12345", False)
    ]

    instance = StringUtils()

    for test_str, expected in test_cases:
        result = instance.is_palindrome(test_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_str}' -> Expected: {expected}, Got: {result}")