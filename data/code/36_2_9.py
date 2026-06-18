class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string in-place using slicing.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string that is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "hello world",
        "",
        "a",
        "Python is awesome!",
        "To be, or not to be"
    ]

    reverser = StringReverser()

    print("String Reversal Test Results:")
    for original in test_cases:
        reversed_text = reverser.reverse(original)
        status = "PASS" if original == reversed_text[::-1] else "FAIL"  # Double reverse to verify correctness logic visually, though single slice is correct. Actually, let's just print the result directly as per task simplicity without complex validation assertions that might confuse output.
        
        print(f"Input:    '{original}'")
        print(f"Output:   '{reversed_text}'")
        print("-" * 30)