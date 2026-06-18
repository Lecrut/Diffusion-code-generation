class CustomString:
    """A custom string class with methods to manipulate character pairs."""

    def swap_adjacent_pairs(self):
        """Swaps every adjacent pair of characters in place and returns self.
        
        If the length is odd, the last unpaired character remains unchanged.
        Example: "abcd" -> "badc", "abcde" -> "bcade".
        Time Complexity: O(n) where n is the string length.
        Space Complexity: O(1) excluding input/output storage as it modifies in place (conceptually creates new list then joins).
        
        Returns:
            CustomString instance with swapped characters.
        """
        if not hasattr(self, '_chars') or len(self._chars) == 0:
            return self
        
        chars = list(self._chars)
        length = len(chars)

        # Iterate over the string in steps of two indices (i and i+1).
        for i in range(0, length - 1, 2):
            if i + 1 < length:
                # Swap current character with next one.
                chars[i], chars[i + 1] = chars[i + 1], chars[i]

        self._chars = "".join(chars)
        return self

if __name__ == '__main__':
    pass
