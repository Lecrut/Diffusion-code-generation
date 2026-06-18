class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        
        Since Python strings are immutable, this method returns a new string 
        with swapped pairs. If there is an odd length string, the last character remains unchanged.

        Args:
            text (str): The input string to process.

        Returns:
            str: A new string with all adjacent characters swapped in pairs.
        
        Examples:
            >>> manipulator = StringManipulator()
            >>> result1 = manipulator.swap_all_pairs("ab")
            >>> print(result1)
            ba
            
            >>> result2 = manipulator.swap_all_pairs("abcd")
            >>> print(result2)
            bacd
            
            >>> result3 = manipulator.swap_all_pairs("abcde")
            >>> print(result3)
            badc e (last char 'e' stays as is due to odd length, though logic keeps it separate)
        """
        if not text:
            return ""

        # Convert string to list for mutability simulation or direct construction
        chars = list(text)
        
        n = len(chars)
        i = 0
        
        while i < n - 1:
            # Swap characters at index i and i+1
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            
            # Move by two steps to process next pair
            i += 2
            
        return "".join(chars)

if __name__ == '__main__':
    manipulator = StringManipulator()

    sample_1 = "ab"
    sample_2 = "abcd"
    sample_3 = "abcdefg"
    
    # Test cases with hard-coded values, no user input required
    
    print("Test 1:", repr(sample_1))
    result_a = manipulator.swap_all_pairs(sample_1)
    print("Result:", repr(result_a), "\n")

    print("Test 2:", repr(sample_2))
    result_b = manipulator.swap_all_pairs(sample_2)
    print("Result:", repr(result_b), "\n")

    print("Test 3:", repr(sample_3))
    result_c = manipulator.swap_all_pairs(sample_3)
    print("Result:", repr(result_c))