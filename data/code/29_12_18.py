class StringReverser:
    """A class that provides methods to reverse strings efficiently."""

    def __init__(self, input_string: str = "") -> None:
        self._original_string = input_string

    @property
    def original(self) -> str:
        return self._original_string

    def reverse(self) -> str:
        """Returns a new string with the characters in reversed order.
        
        This method uses Python's built-in slicing which is implemented efficiently 
        using C-level optimizations, avoiding explicit loops for better performance.
        
        Returns:
            A new string containing the input string's characters in reverse order.
            
        Raises:
            TypeError: If the input argument passed to this instance (not used here) was not a str.
                    Note: The original_string is set during initialization and assumed valid there.
        """
        return self._original_string[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    
    # Test case 1: Simple string
    reverser = StringReverser("Hello")
    result_1 = reverser.reverse()
    
    # Test case 2: Empty string
    empty_reverser = StringReverser("")
    result_empty = empty_reverser.reverse()
    
    # Test case 3: Single character
    single_char_reverser = StringReverser("a")
    result_single = single_char_reverser.reverse()
    
    # Test case 4: Longer string with spaces and punctuation
    complex_string = "Python is awesome!"
    complex_reverser = StringReverser(complex_string)
    result_complex = complex_reverser.reverse()

    print(f"Original: {reverser.original}")
    print(f"Reversed: {result_1}")
    
    print("\n--- Empty String Test ---")
    print(f"Original: '{empty_reverser.original}'")
    print(f"Reversed: '{result_empty}'")

    print("\n--- Single Character Test ---")
    print(f"Original: '{single_char_reverser.original}'")
    print(f"Reversed: '{result_single}'")

    print("\n--- Complex String Test ---")
    print(f"Original: {complex_string}")
    print(f"Reversed: {result_complex}")