class StringCombiner:
    """A class to efficiently join two input strings."""

    def combine(self, str1: str, str2: str) -> str:
        """Joins two strings into a single string with no separator.
        
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

    test_str_1 = "Hello"
    test_str_2 = "World!"

    result = combiner.combine(test_str_1, test_str_2)

    print(result)