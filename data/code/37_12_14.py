class StringCombiner:
    """A class that provides utilities to combine strings."""

    def __init__(self):
        """Initialize the StringCombiner instance with no arguments required."""
        pass

    def combine(self, str1, str2):
        """Efficiently join two input strings.
        
        Args:
            str1 (str): The first string to be combined.
            str2 (str): The second string to be combined.
            
        Returns:
            str: A new string formed by concatenating str1 and str2 in that order.
        """
        return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    combiner = StringCombiner()

    sample_str1 = "Hello"
    sample_str2 = ", World!"

    result = combiner.combine(sample_str1, sample_str2)

    print(result)  # Output: Hello, World!