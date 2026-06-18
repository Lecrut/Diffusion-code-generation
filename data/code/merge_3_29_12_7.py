class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string efficiently using slicing.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: The reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [
        "Hello, World!",
        "",
        "a",
        "Python is awesome.",
        "To be or not to be"
    ]

    reverser = StringReverser()

    for sample in samples:
        reversed_text = reverser.reverse(sample)
        print(f"Original: {sample}")
        print(f"Reversed: {reversed_text}\n")