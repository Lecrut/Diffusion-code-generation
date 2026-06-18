class StringCombiner:
    """A class that provides methods to join strings efficiently."""

    def combine(self, str1: str, str2: str) -> str:
        """Joins two input strings into a single string without extra whitespace.
        
        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.
            
        Returns:
            str: A new string with the inputs concatenated directly.
        """
        return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    combiner = StringCombiner()

    test_str1 = "Hello"
    test_str2 = "World!"

    result = combiner.combine(test_str1, test_str2)

    print(result)  # Output: HelloWorld!