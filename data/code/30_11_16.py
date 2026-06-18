import copy

class CustomString:
    """A custom string-like class with additional methods."""

    def __init__(self, data):
        if not isinstance(data, str):
            raise TypeError("Data must be a string.")
        self._data = list(data)  # Store as mutable list for processing

    @property
    def value(self):
        """Return the current string representation."""
        return "".join(self._data)

    def swap_adjacent_pairs(self):
        """Swaps characters of every adjacent pair in place and returns self.
        
        This method iterates over the list with a step of 2, swapping elements at indices i and i+1 if they exist.
        It handles edge cases such as odd-length strings (where the last character remains unchanged).

        Returns:
            CustomString: The instance itself after modification.
        """
        n = len(self._data)
        for i in range(0, n - 1, 2):
            if i + 1 < n:
                self._data[i], self._data[i + 1] = self._data[i + 1], self._data[i]
        
        return self

if __name__ == '__main__':
    pass
