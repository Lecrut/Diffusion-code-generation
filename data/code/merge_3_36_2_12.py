class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses a given string.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: A new string with the characters in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "A man a plan a canal Panama!"
    ]

    reverser = StringReverser()

    print("String Reversal Test Results:")
    print("-" * 30)

    for original in test_cases:
        reversed_str = reverser.reverse(original)
        status = "PASS" if original == reversed_str[::-1] else "FAIL"
        # Note: The above check is redundant since the method always returns a true reverse,
        # but included to demonstrate usage logic clearly.
        
        print(f"Input:    '{original}'")
        print(f"Output:   '{reversed_str}'")
        print(f"Status: {status}\n")

    # Verify specific example manually for clarity in output
    sample = "Hello, World!"
    result = reverser.reverse(sample)
    assert result == "!dlroW ,olleH", f"Expected '!dlroW ,olleH', got '{result}'"
    
    print("All assertions passed successfully.")