import string

class StringCombiner:
    """A class that provides utility methods for combining strings."""

    def combine(self, str1: str, str2: str) -> str:
        """Efficiently joins two input strings with a space in between.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            str: A new string formed by joining the arguments separated by a space.

        Examples:
            >>> combiner = StringCombiner()
            >>> result = combiner.combine("Hello", "World")
            'Hello World'
        """
        return f"{str1} {str2}"

if __name__ == "__main__":
    # Hard-coded sample values to demonstrate functionality without external input.
    string_combiner = StringCombiner()

    str_a = "Python"
    str_b = "is powerful"

    combined_result = string_combiner.combine(str_a, str_b)
    print(combined_result)  # Expected Output: Python is powerful