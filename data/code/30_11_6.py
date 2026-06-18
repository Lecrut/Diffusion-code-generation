import copy

class CustomString:
    """A custom string-like class with additional manipulation methods."""

    def __init__(self, input_str=None):
        if input_str is None:
            self._data = ""
        else:
            # Normalize the input to a list of characters for mutability
            try:
                self._data = [c for c in input_str]
            except TypeError:
                raise ValueError("Input must be a string-like object.")

    def __str__(self):
        return "".join(self._data)

    def swap_adjacent_pairs(self):
        """
        Swaps the characters of every adjacent pair within the instance.
        
        This method modifies the underlying character list in-place.
        It processes pairs from left to right, swapping (0,1), then (2,3), etc.
        Any odd-length string will leave the last character unchanged.

        Returns:
            None (modifies self._data in place)
        
        Example:
            >>> s = CustomString("abcd")
            >>> s.swap_adjacent_pairs()
            >>> print(s)
            'badc'
            
            >>> # Edge case: odd length string "abc" -> "bac"
            >>> t = CustomString("abc")
            >>> t.swap_adjacent_pairs()
            >>> print(t)
            'bac'
        """
        n = len(self._data)
        
        # Iterate through the list with a step of 2.
        for i in range(0, n - 1, 2):
            # Swap current character at index i with next character at index i+1
            self._data[i], self._data[i + 1] = self._data[i + 1], self._data[i]

    def __repr__(self):
        return f"CustomString('{str(self)}')"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Even length string with visible swap effect
    s1 = CustomString("Hello")
    print(f"Original (Sample 1): {s1}")
    s1.swap_adjacent_pairs()
    print(f"After swap:           '{s1}'\n")

    # Sample 2: Odd length string where the last character remains fixed relative to its pair logic
    s2 = CustomString("Python")
    original_s2_str = str(s2)
    s2.swap_adjacent_pairs()
    print(f"Original (Sample 2): {original_s2_str}")
    print(f"After swap:           '{s2}'\n")

    # Sample 3: Single character string (edge case, no pairs to swap)
    s3 = CustomString("X")
    original_s3_str = str(s3)
    s3.swap_adjacent_pairs()
    print(f"Original (Sample 3): {original_s3_str}")
    print(f"After swap:           '{s3}'\n")

    # Sample 4: String with mixed case and numbers to ensure robustness
    s4 = CustomString("a1b2c3d4e5f6g7h8i9j0k")
    original_s4_str = str(s4)
    s4.swap_adjacent_pairs()
    print(f"Original (Sample 4): {original_s4_str}")
    print(f"After swap:           '{s4}'\n")

    # Sample 5: Empty string edge case
    empty_str = CustomString("")
    original_empty_str = str(empty_str)
    empty_str.swap_adjacent_pairs()
    print(f"Original (Empty):     '{original_empty_str}'")
    print(f"After swap:           '{empty_str}'\n")

    # Sample 6: Two character string (minimum pair)
    s6 = CustomString("AB")
    original_s6_str = str(s6)
    s6.swap_adjacent_pairs()
    print(f"Original (Sample 6): {original_s6_str}")
    print(f"After swap:           '{s6}'\n")

    # Demonstrate that the method modifies in-place and does not return a new string object
    test_obj = CustomString("12345")
    result_of_swap = test_obj.swap_adjacent_pairs()  # Should be None
    
    print(f"Return value of swap_adjacent_pairs(): {result_of_swap}")
    
    if original_s6_str != str(s6):
        pass