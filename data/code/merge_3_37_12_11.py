class StringCombiner:
    """A class that provides methods to combine strings efficiently."""

    def combine(self, str1: str, str2: str) -> str:
        """
        Joins two input strings into a single string.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            str: A new string formed by concatenating str1 and str2.
        """
        return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    combiner = StringCombiner()

    result = combiner.combine("Hello", "World")
    print(result)  # Expected output: HelloWorld