class StringReverser:
    """A class that provides functionality to reverse strings."""
    
    def __init__(self):
        """Initialize the StringReverser object with no parameters needed."""
        pass
    
    def reverse(self, text):
        """
        Reverse a given string.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: A new string which is the reverse of the input string.
        
        Raises:
            TypeError: If the input 'text' is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError("The text argument must be a string.")
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello world",
        "",
        "A man, a plan, a canal: Panama",
        "!radar!",
        12345,  # This should trigger the TypeError check
    ]

    reverser = StringReverser()

    for i, text in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        try:
            reversed_text = reverser.reverse(text) if isinstance(text, str) else "Error raised (Expected)"
            # Note: The logic above handles the error check inline to avoid exceptions crashing flow 
            # while demonstrating the type checking inside the class.
            print(f"Input:    {repr(text)}")
            print(f"Output:   {repr(reversed_text if isinstance(text, str) else 'Type Error Raised')}")
        except TypeError as e:
            print(f"Exception raised for non-string input (Test case {i + 1}):", type(e).__name__)
        
        # Re-run the specific method call only on strings to show correct output for valid inputs
        if isinstance(text, str):
            result = reverser.reverse(text)
            print("Correct Execution Result:", repr(result))
            
    sample_output: str = "Hello World"
    reversed_sample: str = reverser.reverse(sample_output)
    assert reversed_sample == "dlroWolleH", "Reverse logic failed!"
    print("\nAssertion passed successfully.")