class StringCombiner:
    """A class designed to efficiently join two input strings."""

    def combine(self, str1: str, str2: str) -> str:
        """
        Joins two input strings into a single string.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            str: The concatenated result of the two strings.
        """
        return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction.
    combiner = StringCombiner()
    
    string_one = "Hello"
    string_two = ", World!"

    result = combiner.combine(string_one, string_two)
    print(result)  # Expected Output: Hello, World!