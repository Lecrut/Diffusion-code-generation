class StringCombiner:
    """A class to efficiently join two input strings."""

    def combine(self, str1: str, str2: str) -> str:
        """Joins two input strings into a single string.
        
        Args:
            str1 (str): The first string operand.
            str2 (str): The second string operand.
            
        Returns:
            str: A new string that is the concatenation of str1 and str2.
        """
        return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sampler = StringCombiner()

    s1 = "Hello"
    s2 = ", World!"

    result = sampler.combine(s1, s2)

    print(result)  # Output: Hello, World!