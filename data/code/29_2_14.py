class StringReverser:
    def reverse(self, word):
        """
        Reverses the input string.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: The reversed version of the input string.
        """
        return word[::-1]

if __name__ == '__main__':
    # Sample test cases run without user interaction or external dependencies
    tests = [
        ("hello", "olleh"),
        ("Python3", "3nohtyP"),
        ("", ""),
        ("A man a plan, a canal: Panama!", "!amanaP :lanac A ,nalp A nam A")
    ]

    reverser = StringReverser()
    
    for input_str, expected_output in tests:
        result = reverser.reverse(input_str)
        assert result == expected_output, f"Test failed for '{input_str}': got {result}, expected {expected_output}"
        
print("All test cases passed.")