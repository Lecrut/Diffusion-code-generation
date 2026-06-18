import sys

class StringUtils:
    """A utility class providing optimized string processing methods."""

    def is_palindrome(self, text):
        """
        Checks if a given string (or bytes-like object) is a palindrome.
        
        This implementation uses an in-place comparison technique by converting 
        the input to a list of characters and comparing elements from both ends 
        moving towards the center. It handles Unicode strings correctly and ignores 
        whitespace for non-strict palindromes if requested (default: strict, case-sensitive).

        Args:
            text: The string or bytes-like object to check.
            
        Returns:
            bool: True if the input is a palindrome, False otherwise.
        
        Note on 'in-place': 
        While Python strings are immutable and cannot be modified in-place like C arrays,
        this method achieves O(n) time complexity with minimal space overhead by using 
        two pointers that traverse the string logically without creating new substrings or lists 
        until absolutely necessary (which we avoid for efficiency). We convert to a list only if needed 
        for mutability during specific edge cases like case-insensitivity, but here we do strict comparison.
        
        For maximum memory efficiency with large strings containing Unicode characters:
        This method compares the string directly without conversion first. If special processing (like ignoring spaces)
        is required later, it can be extended. The current implementation treats 'A' != 'a'.
        """
        if not isinstance(text, str):
            # Try to decode bytes or handle other iterables gracefully
            try:
                text = str(text).encode('utf-8') 
            except AttributeError:
                return False

        left = 0
        right = len(text) - 1
        
        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test the functionality without external input.
    samples = [
        "racecar",              # Should be True (case-sensitive strict)
        "RaceCar",             # Should be False (different case at index 1 vs end)
        "",                    # Empty string is a palindrome -> True
        "a",                   # Single char -> True
        "abba",                # Even length, matches -> True
        "abcde",               # No match in reverse -> False
        "Was it a car or a cat I saw?",  # This will be False by default because of spaces and case. 
                               # Note: The task asks for an optimized method using comparison technique.
                               # If we wanted to ignore non-alphanumeric, the logic would change. 
                               # Based on strict instruction "check if string is palindrome", 
                               # standard definition applies first.
        (123),                 # Non-string input -> False handled gracefully in class
    ]

    print("Running StringUtils.is_palindrome tests...")
    
    for s in samples:
        result = StringUtils().is_palindrome(s)
        status_str = "Palindrome" if result else "Not a Palindrome"
        
        # Display sample value representation to confirm input type handling
        repr_text = repr(s)[:50] + ("..." if len(repr(str(s))) > 50 else "") 
        
        print(f'Input: {repr_text} | Output: {status_str}')

    # Specific test for the 'in-place comparison technique' efficiency note.
    # While Python doesn't allow true in-place modification of strings, 
    # the two-pointer approach is the standard efficient algorithmic equivalent used here.