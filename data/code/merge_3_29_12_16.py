class StringReverser:
    def reverse(self, text: str) -> str:
        """
        Reverses a given string efficiently using slicing.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string that is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Hello, World!",
        "",
        "A man a plan a canal Panama",
        "Python is awesome"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for original in samples:
        reversed_str = reverser.reverse(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_str}"\n')