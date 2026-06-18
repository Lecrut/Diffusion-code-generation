class StringCombiner:
    """A class that provides methods to manipulate strings."""

    def combine(self, str1: str, str2: str) -> str:
        """Efficiently joins two input strings without creating unnecessary intermediate objects.
        
        Args:
            str1 (str): The first string operand.
            str2 (str): The second string operand.
            
        Returns:
            str: A new string formed by concatenating str1 and str2.
        """
        return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    combiner = StringCombiner()

    result_1 = combiner.combine("Hello", "World")
    print(f"Result 1: {result_1}")

    result_2 = combiner.combine("", "")
    print(f"Result 2: '{result_2}'")