class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string in place using object-oriented design principles.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string which is the reverse of the input text.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for original in test_cases:
        reversed_str = reverser.reverse(original)
        print(f"Original: '{original}' -> Reversed: '{reversed_str}'")