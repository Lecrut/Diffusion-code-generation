class SubstringExtractor:
    def __init__(self):
        pass
    
    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently finds and returns all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to search for substrings.
            k (int): The desired length of the substrings.
            
        Returns:
            list[str]: A sorted list containing unique substrings of length k.
            
        Raises:
            ValueError: If k is not a positive integer or if k exceeds the length of target_string.
        """
        # Input validation
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k must be a positive integer.")
        
        n = len(target_string)
        if k > n:
            return []

        unique_substrings = set()
        
        # Efficiently extract substrings using sliding window logic implicitly via slicing
        for i in range(n - k + 1):
            substring = target_string[i : i + k]
            unique_substrings.add(substring)
            
        return sorted(list(unique_substrings))

if __name__ == '__main__':
    extractor = SubstringExtractor()
    
    # Hard-coded sample values to ensure no user input or file access is required
    test_string_1 = "abcdef"
    k_value_1 = 2
    
    test_string_2 = "aaaaa"
    k_value_2 = 3
    
    result_set_1 = extractor.get_unique_substrings(test_string_1, k_value_1)
    
    # Print results for the sample cases to verify functionality without external input
    print(f"Unique substrings of length {k_value_1} in '{test_string_1}':")
    print(result_set_1)
    
    result_set_2 = extractor.get_unique_substrings(test_string_2, k_value_2)
    
    print(f"\nUnique substrings of length {k_value_2} in '{test_string_2}':")
    print(result_set_2)