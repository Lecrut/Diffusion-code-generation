class StringReverser:
    """A class designed to reverse strings efficiently using object-oriented principles."""

    def __init__(self, initial_string=None):
        """Initialize the StringReverser with an optional string value."""
        if initial_string is not None and isinstance(initial_string, str):
            self._data = list(initial_string)
        else:
            self._data = []

    @property
    def data(self):
        """Return a copy of the internal character list to prevent external modification."""
        return self._data.copy()

    @classmethod
    def from_string(cls, s):
        """Create an instance efficiently from a string argument.
        
        Args:
            s (str): The input string to reverse.
            
        Returns:
            StringReverser: A new instance containing the reversed characters.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        # Efficiently construct list from string and immediately reverse it
        return cls(list(reversed(list(s))))

    def reverse(self):
        """Reverse the internal character list in-place using two-pointer technique.
        
        Returns:
            StringReverser: Self, updated with reversed data.
            
        Raises:
            RuntimeError: If an error occurs during reversal (unlikely for lists).
        """
        try:
            left = 0
            right = len(self._data) - 1

            while left < right:
                # Swap elements at current pointers
                self._data[left], self._data[right] = self._data[right], self._data[left]
                left += 1
                right -= 1
            
            return self
        except Exception as e:
            raise RuntimeError(f"Failed to reverse string data: {e}")

    def __str__(self):
        """Return a string representation of the reversed content."""
        return "".join(self._data)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test Case 1: Simple alphanumeric string
    test_input_1 = "Hello, World!"
    
    # Create instance and reverse using the method directly
    reverser_1 = StringReverser(test_input_1)
    reversed_result_1 = reverser_1.reverse()

    print(f"Original: {test_input_1}")
    print(f"Reversed: {reversed_result_1.data}\n")  # Accessing .data to show list, or just str(reversed_result_1) for string
    
    # Test Case 2: Using the class method from_string (returns already reversed instance as per design note in comment above? 
    # Wait, my implementation of __init__ and reverse logic needs clarification based on typical expectations.
    # Usually 'reverse' reverses what is currently inside. Let's ensure standard behavior:
    # 1. Init with string -> stores it normally.
    # 2. Call reverse() -> flips the stored list in place.
    
    test_input_2 = "Python Programming"
    r_2 = StringReverser(test_input_2)
    result_r_2 = r_2.reverse()

    print(f"Original: {test_input_2}")
    print(f"Reversed: {''.join(result_r_2.data)}")