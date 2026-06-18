class StringUtils:
    """A utility class providing string manipulation methods."""

    def is_palindrome(self, text: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        The method uses two pointers (left and right) starting from the ends of the 
        character sequence to compare characters inward until they meet or cross.
        This approach avoids creating additional data structures, ensuring O(1) space complexity
        relative to string length for read-only access.

        Args:
            text (str): The input string to check. Non-alphabetic characters are ignored 
                        based on the logic that a palindrome typically considers only letters;
                        however, strictly following "in-place comparison" without filtering implies
                        checking exact character sequence including spaces/punctuation unless specified otherwise.
                        Given the strict constraint of in-place technique for maximum efficiency 
                        and typical use cases where case-insensitivity might be expected but isn't explicitly requested:
                        We will perform a direct check on all characters as is, which allows true O(1) space 
                        without modifying the string object itself (strings are immutable). If modification was intended
                        to simulate in-place swapping of mutable structures like lists or bytearray, that would alter memory layout.
                        
        Returns:
            bool: True if text is a palindrome, False otherwise.

        Note on "In-Place": Since Python strings are immutable, true in-place reversal/swapping isn't possible without 
        converting to a list/bytearray (which uses extra space) or simply iterating with two pointers (the latter being the 
        most efficient algorithmic pattern often colloquially referred to as 'in-place' logic). This implementation uses 
        the two-pointer approach which is the standard optimal solution for this problem.
        
        If the requirement implies ignoring non-alphanumeric characters and case, it should be noted here: 
        Currently, this checks exact character match including spaces/punctuation and preserves original casing.
        """
        left = 0
        right = len(text) - 1
        
        # Two-pointer approach to compare characters from both ends moving inward
        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test the functionality without user input
    
    # Test cases including edge cases and standard palindromes
    samples = [
        "racecar",           # Standard palindrome
        "A man a plan a canal Panama",  # With spaces (assuming case-sensitive check here) -> False due to 'a' vs 'A' if strict, but let's see exact match logic. Actually standard is usually lowercased or filtered. The prompt says 'in-place comparison'. Let's stick to raw string chars for maximum efficiency and literal interpretation unless specified otherwise.
        "madam",             # Standard palindrome
        "",                  # Empty string
        "hello",             # Not a palindrome
        "12321",             # Numeric digits
    ]

    test_cases = [
        ("racecar", True),
        ("A man a plan a canal Panama", False),  # Case sensitive check: 'a' != 'P', space matches, etc. But wait, usually these examples imply normalization. However, the prompt is specific about efficiency and in-place technique without specifying content transformation rules other than palindrome definition. 
        # Let's define palindrome strictly as reading same forwards and backwards exactly as given to avoid assumptions not requested (like ignore spaces).
        ("madam", True),
        ("hello", False),
        ("12321", True),
    ]

    for text, expected in test_cases:
        result = StringUtils().is_palindrome(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] '{text}' -> {result} (Expected: {expected})")