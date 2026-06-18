class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, word):
        """
        Reverses the input string in place if it is a list of characters,
        or returns a new reversed string if the input is already a string.
        
        Args:
            word (str | list[str]): The string to be reversed. If a list 
                                   of characters is provided, it will be joined 
                                   and then reversed.
            
        Returns:
            str: A new string with the characters in reverse order.

        Raises:
            TypeError: If 'word' is not a string or a list of strings/characters.
        """
        if isinstance(word, str):
            return word[::-1]
        elif isinstance(word, (list, tuple)):
            # Convert to string first by joining characters, then reverse
            try:
                temp_str = "".join(str(item) for item in word)
                return temp_str[::-1]
            except TypeError as e:
                raise TypeError("List must contain only strings or other types convertible to str.") from e
        else:
            raise TypeError("Input must be a string, list of characters, or tuple of characters.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    tester = StringReverser()

    sample1 = "hello"
    result1 = tester.reverse(sample1)
    
    sample2 = ["h", "e", "l", "l", "o"]
    result2 = tester.reverse(sample2)
    
    print(f"Original: {sample1}")
    print(f"Reversed: {result1}")

    print("\n--- List Input ---")
    print(f"Original list: {sample2}")
    print(f"Reversed string from list: {result2}")