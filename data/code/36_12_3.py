class StringReverser:
    def reverse(self, text):
        """
        Reverses the input string.
        
        Args:
            text (str): The string to be reversed.
            
        Returns:
            str: The reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello world",
        "",
        "a",
        "Python is great!",
    ]

    reverser = StringReverser()

    print("String Reversal Test Results:")
    for original in test_cases:
        reversed_text = reverser.reverse(original)
        print(f"Original:   '{original}'")
        print(f"Reversed:   '{reversed_text}'")
        print("-" * 20)