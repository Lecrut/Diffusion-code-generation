class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string in-place without creating intermediate lists if possible,
        using two-pointer technique to swap characters from both ends towards the center.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string that is the reverse of the input.
        """
        # Convert to list for mutability, then back to string at end if needed,
        # but since strings are immutable in Python, we return a new one efficiently.
        chars = list(text)
        left, right = 0, len(chars) - 1
        
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
        return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        "Hello, World!",
        "",
        "A",
        "Python Programming"
    ]

    reverser = StringReverser()

    for text in test_cases:
        reversed_text = reverser.reverse(text)
        print(f'Original: "{text}"')
        print(f'Reversed: "{reversed_text}"\n')