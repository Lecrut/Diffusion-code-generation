class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text: str) -> str:
        """
        Returns a new string with characters in reversed order.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string containing the characters of `text` in reverse order.
            
        Note: This method creates and returns a new object; it does not 
        modify the original input string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external inputs
    
    # Sample 1: Simple string with spaces
    sample_1 = "Hello, World!"
    
    # Create an instance and call the method
    reverser = StringReverser()
    
    result_1 = reverser.reverse(sample_1)
    
    print(f"Original: '{sample_1}'")
    print(f"Reversed: '{result_1}'\n")

    # Sample 2: Empty string (edge case)
    sample_2 = ""
    result_2 = reverser.reverse(sample_2)
    assert result_2 == "", "Empty string handling failed."

    # Sample 3: Single character
    sample_3 = "a"
    result_3 = reverser.reverse(sample_3)
    assert result_3 == "a", "Single character reversal failed."

    # Output the results for samples 2 and 3 to verify edge cases run correctly without prompts
    print(f"Sample Empty String - Input: '{sample_2}', Output: '{result_2}'")
    print(f"Sample Single Char - Input: '{sample_3}', Output: '{result_3}'")
    
    # Final confirmation if all assertions passed (implicit in running this block)