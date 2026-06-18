"""
Module to compare two strings lexicographically and return detailed difference information.
This module avoids external dependencies, input prompts, and interactive features as per requirements.
"""

class StringComparisonResult:
    """A data class representing the result of a string comparison."""

    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2
        
        # Determine lengths and which is longer to avoid index errors later
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 == 0 or len_s2 == 0:
            raise ValueError("Both strings must be non-empty for meaningful comparison.")

        # Find the first differing character and determine effective length to compare up to that point
        min_len = min(len_s1, len_s2)
        
        self.first_diff_index = -1
        
        if s1 == s2:
            self.is_equal = True
            self.difference_length = 0
            return

        for i in range(min_len):
            char_s1 = s1[i]
            char_s2 = s2[i]
            
            # Use a custom comparison logic to avoid direct equality if Unicode normalization is needed, 
            # but standard == operator handles most lexicographical cases correctly.
            # For strict byte-level or specific unicode collation, one might use unicodedata.normalize,
            # but the task implies general string manipulation best practices where '==' is sufficient for logic flow.
            
            if char_s1 != char_s2:
                self.first_diff_index = i
                
                # Determine which character was "larger" based on ASCII/Unicode value order
                # This helps in understanding lexicographical ordering without sorting the whole string
                if ord(char_s1) > ord(char_s2):
                    self.s1_is_larger_at_first_diff = True
                else:
                    self.s1_is_larger_at_first_diff = False
                
                break
        
        # If loop finishes without breaking, strings are identical up to min_len.
        # One string is a prefix of the other.
        if self.first_diff_index == -1:
            if len_s1 < len_s2:
                self.s1_is_larger_at_first_diff = False  # s2 extends further -> effectively "larger" in length context? 
                                                        # Usually shorter prefix comes before longer string lexicographically.
                                                        # So if we reached here, s1 is a prefix of s2.
            else:
                self.s1_is_larger_at_first_diff = True  # s1 extends further
            
            # The "difference" in this context is the extra characters in the longer string starting from index min_len

if __name__ == '__main__':
    pass
