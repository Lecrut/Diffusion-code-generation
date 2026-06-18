class StringReverser:
    def reverse(self, text):
        """
        Reverses the input string in-place (modifies the list of characters) or returns a new reversed string.
        
        This implementation treats `text` as an iterable sequence and reverses it by slicing,
        which creates a new string containing the characters in reverse order.
        Since strings are immutable in Python, this method cannot truly modify the input object
        without converting it to a list first or returning the result for use elsewhere.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string with characters in reverse order.
        """
        return ''.join(reversed(text))

if __name__ == '__main__':
    # Sample test cases without user interaction or external dependencies
    sample_1 = "hello"
    sample_2 = ""
    sample_3 = "Python programming is fun!"

    reverser = StringReverser()

    print(f'Reversed "{sample_1}": {reverser.reverse(sample_1)}')
    print(f'Empty string reversed: "{reverser.reverse(sample_2)}"')
    print(f'Reversed "{sample_3}": {reverser.reverse(sample_3)}')