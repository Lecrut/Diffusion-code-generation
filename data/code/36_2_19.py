class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string in-place using slicing to create a new reversed string.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string which is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "A"
    ]

    reverser = StringReverser()

    print("String Reversal Test Results:")
    for original in test_cases:
        reversed_text = reverser.reverse(original)
        status = "PASS" if list(reversed_text) == list(original[::-1]) else "FAIL"
        print(f"[{status}] Input: '{original}' -> Output: '{reversed_text}'")