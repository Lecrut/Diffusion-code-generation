class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, word):
        """
        Reverses the input string in-place (modifies self).

        Args:
            word (str): The string to be reversed. This argument is kept for 
                        interface consistency but not strictly used as 'self' 
                        modifies internal state if needed or just returns new logic.
        
        Returns:
            str: A new string that is the reverse of the input `word`.

        Note: Since Python strings are immutable, this method creates and returns a reversed copy.
              If strict in-place modification were required on an object holding data, 
              one would modify internal attributes; here we return the result directly as per standard practice.
        """
        # Using slicing to reverse the string efficiently
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for word in test_cases:
        reversed_word = reverser.reverse(word)
        print(f'Original: "{word}" -> Reversed: "{reversed_word}"')