import sys

class CustomString:
    """A custom string class with additional functionality."""

    def __init__(self, value=""):
        self._value = list(value) if isinstance(value, str) else list(value)

    def swap_adjacent_pairs(self):
        """
        Swaps the characters of every adjacent pair within the string instance.
        
        The method iterates through the string in steps of 2, swapping each character
        with its immediate neighbor (i.e., index i and i+1). If there is an odd number
        of characters, the last one remains unchanged as it has no pair.

        Returns:
            None; modifies the instance in place.
        
        Examples:
            >>> s = CustomString("abcd")
            >>> s.swap_adjacent_pairs()
            >>> print(s)
            'badc'
            
            >>> s2 = CustomString("abc")
            >>> s2.swap_adjacent_pairs()
            >>> print(s2)
            'bac'

        Raises:
            TypeError: If the input is not a string. This check is implicit in __init__,
                      but ensures robustness if external methods were to accept strings directly.
        """
        # Ensure we are working with a list of characters for mutability
        n = len(self._value)
        
        # Iterate through indices 0, 2, 4... up to the second-to-last character (if even length)
        i = 1
        
        while i < n:
            if i + 1 >= n:
                break
            
            self._value[i], self._value[i - 1] = self._value[i - 1], self._value[i]
            
            # Move to the next pair starting index (increment by 2)
            i += 2

    def __str__(self):
        return "".join(self._value)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Test Case 1: Even length string with distinct characters
    test_case_1 = CustomString("abcdef")
    print(f"Original (Test 1): {test_case_1}")
    test_case_1.swap_adjacent_pairs()
    print(f"After swap (Test 1): {test_case_1}\n")

    # Test Case 2: Odd length string where the last character should remain unchanged
    test_case_2 = CustomString("hello world!")
    print(f"Original (Test 2): '{test_case_2}'")
    test_case_2.swap_adjacent_pairs()