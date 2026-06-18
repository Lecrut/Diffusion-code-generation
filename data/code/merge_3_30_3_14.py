import string

class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Performs an in-place style operation on a list of characters derived from the input string,
        swapping adjacent pairs (indices 0-1, 2-3, etc.). Returns the new string.
        
        Note: Python strings are immutable, so true "in-place" modification returning the same object reference is not possible.
        This method converts to a list of characters for mutation and returns a new string representing the result.
        """
        chars = list(text)
        n = len(chars)
        
        # Iterate through the list with a step of 2, swapping each pair if both elements exist
        for i in range(0, n - 1, 2):
            j = i + 1
            if j < n:
                chars[i], chars[j] = chars[j], chars[i]
        
        return ''.join(chars)

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no external inputs are needed
    sample_inputs = [
        "abcdef",
        "aabbccdd",
        "hello",  # Odd length string ending in a single character
        "",       # Empty string edge case
        "xy"      # Minimal pair
    ]

    manipulator = StringManipulator()

    for test_text in sample_inputs:
        result = manipulator.swap_all_pairs(test_text)
        print(f"Input:  '{test_text}'")
        print(f"Output: '{result}'\n")