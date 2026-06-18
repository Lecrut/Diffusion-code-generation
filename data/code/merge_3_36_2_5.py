class StringReverser:
    """A class that provides methods to manipulate string operations."""
    
    def reverse(self, text):
        """Returns a new reversed version of the input string without modifying it in-place.
        
        Args:
            text (str): The string to be reversed.
            
        Returns:
            str: A newly created string with characters in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, network access, or file operations are used.
    
    reverser = StringReverser()
    
    test_cases = [
        "Hello",
        "Python Programming",
        "",
        "A"
    ]
    
    print("String Reversal Results:")
    for original in test_cases:
        reversed_text = reverser.reverse(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_text}"\n')