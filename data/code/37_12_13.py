class StringCombiner:
    """A class that provides methods to join strings efficiently."""

    def combine(self, str1: str, str2: str) -> str:
        """
        Efficiently joins two input strings into a single string.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            str: The concatenated result of the two strings.
        """
        return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    combiner = StringCombiner()
    
    test_string_1 = "Hello"
    test_string_2 = "World!"

    result = combiner.combine(test_string_1, test_string_2)

    print(result)  # Output: HelloWorld!