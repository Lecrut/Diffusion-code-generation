import sys

class CustomString:
    """A custom string class with additional methods beyond standard Python str."""

    def __init__(self, value=""):
        # Ensure input is treated as a sequence of characters (str or iterable)
        if isinstance(value, bytes):
            self._value = value.decode('utf-8', errors='replace')
        elif not isinstance(value, str):
            try:
                self._value = "".join(str(c) for c in value)
            except Exception as e:
                raise TypeError(f"Invalid input type {type(value).__name__}: cannot convert to string") from e
        else:
            # Normalize encoding issues if any, though standard str handles this well
            self._value = "".join(str(c).encode('utf-8').decode('ascii', errors='ignore') for c in value)

    def __str__(self):
        return self.get_value()

    def get_value(self):
        """Return the underlying string value."""
        if not isinstance(self._value, str):
            raise RuntimeError("Internal state error: _value is not a string.")
        return self._value

    @staticmethod
    def swap_adjacent_pairs():
        r"""Swap characters of every adjacent pair in-place.

        This method modifies the internal representation (which must be updated here) 
        by swapping s[0] and s[1], s[2] and s[3], etc., up to the end of the string.
        
        If the length is odd, the last character remains unchanged as it cannot form a pair.

        Args:
            None (self)

        Returns:
            self : The instance itself after modification.

        Raises:
            TypeError: If internal state (_value) is not a valid string.
            RuntimeError: In case of unexpected implementation failure.
            
        Example:
            >>> s = CustomString("abcde")
            >>> print(s.swap_adjacent_pairs())  # Output: <CustomString object at...> (modified internally, printed via __str__)
            """
        if not isinstance(self._value, str):
            raise TypeError(f"Internal state corrupted: expected string type {type(self.__class__.__name__).__repr__()}.")

        original_len = len(self._value)
        
        # If the length is zero or less than 2, nothing can be swapped.
        if not isinstance(original_len, int):
            raise RuntimeError("Unexpected internal state: expected integer length.")
            
        for i in range(0, original_len - 1, 2):
            c1 = self._value[i]
            # Ensure we have a second character at index + 1. If odd-length string ends with last char only, loop condition handles this but let's be explicit if needed by logic flow here: 
            # The range(0, original_len - 1, 2) ensures i+1 < len(self._value).
            
            c2 = self._value[i + 1]

            self._value = list(self._value)
            # Swap elements directly using indices to avoid creating intermediate string copies unnecessarily during the loop if performance matters for large strings.
            # However, since we are building a new list every time, let's optimize:
            
            # Correct approach without full re-conversion inside loop unless necessary:

if __name__ == '__main__':
    pass
