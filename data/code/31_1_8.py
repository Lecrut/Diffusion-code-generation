import sys

class StringUtils:
    def is_palindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome using an in-place comparison technique.
        
        Since Python strings are immutable and cannot be modified in-place efficiently 
        without converting to mutable structures (like lists), the most efficient approach 
        for general purpose use within Python involves using two pointers moving towards 
        each other on indices of the original string, avoiding extra space allocation if possible,
        though technically 'in-place' modification isn't feasible for strings directly.
        
        However, adhering to the spirit of "two-pointer" technique which compares characters from both ends:
        This implementation is optimized by only iterating half the length of the string 
        and comparing corresponding character indices without constructing new intermediate lists if avoided.

        Args:
            s (str): The input string to check
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        # Handle edge cases for empty strings or single characters immediately
        len_s = len(s)
        
        left_ptr = 0
        right_ptr = len_s - 1

        while left_ptr < right_ptr:
            char_left = s[left_ptr]
            
            if char_left != s[right_ptr]:
                return False
            
            left_ptr += 1
            right_ptr -= 1
        
        # If the loop completes without returning False, it's a palindrome
        return True

if __name__ == '__main__':
    test_cases = [
        "radar",           # Should be True
        "hello",           # Should be False
        "",                # Should be True (empty string)
        "a",               # Should be True (single char)
        "Was it a car?"   # Should be False (case sensitive by default, has spaces if treated as literal but usually palindromic check ignores non-alphanumeric or is strict. Here strict comparison including spaces and case). Let's adjust expectation: 'r'!='a', so false anyway. Actually 'W' != '?'
    ]

    # Run tests on hard-coded sample values without external input
    for test_str in test_cases:
        result = StringUtils().is_palindrome(test_str)
        print(f'String: "{test_str}" -> Palindrome: {result}')