class StringReverser:
    """A class designed to reverse strings efficiently using object-oriented principles."""

    def __init__(self, input_string: str = None):
        """Initialize with an optional initial string."""
        self._internal_data: str = input_string if input_string is not None else ""

    @property
    def reversed_value(self) -> str:
        """Returns the reversed version of the internal data without exposing state directly.

        Returns:
            The reverse of `self._internal_data`.
        """
        return self._internal_data[::-1]

    def reverse(self) -> str:
        """Reverses the current string stored in `_internal_data` and returns it.

        This method is designed to be immutable regarding the internal state; 
        if an argument-based reversal is desired on a copy, that can be handled here or via logic extension.
        
        Returns:
            The reversed string of `self._internal_data`.
        """
        # Efficiently reverse using slice assignment which creates a new string object immediately
        result = self._internal_data[::-1]
        return result

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    
    # Test case 1: Basic string reversal
    test_input_1 = "Hello, World!"
    reverser_1 = StringReverser(test_input_1)
    
    print(f"Original ({test_input_1}):")
    result_1 = reverser_1.reverse()
    print(f"Reversed: {result_1}")
    
    # Test case 2: Empty string
    test_input_2 = ""
    reverser_2 = StringReverser(test_input_2)
    print(f"\nOriginal ('{test_input_2}'):")
    result_2 = reverser_2.reverse()
    print(f"Reversed: '{result_2}'")

    # Test case 3: Single character string (edge case handled by OOP and logic consistency check)
    test_input_3 = "A"
    reverser_3 = StringReverser(test_input_3)
    
    # Demonstrate property access alongside method call to show encapsulation benefits
    print(f"\nOriginal ({test_input_3}):")
    result_3_prop = reverser_3.reversed_value
    result_3_method = reverser_3.reverse()
    print(f"Reversed via Property: {result_3_prop}")
    print(f"Reversed via Method:  {result_3_method}")