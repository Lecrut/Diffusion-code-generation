class StringCombiner:
    def combine(self, str1: str, str2: str) -> str:
        """
        Efficiently joins two input strings into a single string.
        
        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.
            
        Returns:
            str: The concatenated result of str1 and str2.
        """
        return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    combiner = StringCombiner()
    
    test_str1 = "Hello"
    test_str2 = "World!"
    
    result = combiner.combine(test_str1, test_str2)
    print(result)