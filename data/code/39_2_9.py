class SubstringExtractor:
    def __init__(self):
        pass
    
    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find and return all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to extract substrings from.
            k (int): The desired length of each substring.
            
        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
            
        Raises:
            ValueError: If k is less than 1 or greater than the length of target_string.
        """
        if not isinstance(target_string, str):
            raise TypeError("target_string must be a string.")
        
        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be a positive integer.")
            
        n = len(target_string)
        if k > n:
            return []

        unique_substrings = set()
        
        # Efficiently extract substrings using slicing and add to a set for uniqueness
        for i in range(n - k + 1):
            substring = target_string[i : i + k]
            unique_substrings.add(substring)
            
        return sorted(list(unique_substrings))

if __name__ == '__main__':
    extractor = SubstringExtractor()
    
    # Hard-coded sample values as per requirements (no user input, args, or files)
    test_string_1 = "banana"
    k_value_1 = 2
    
    test_string_2 = "programming"
    k_value_2 = 3
    
    result_1 = extractor.get_unique_substrings(test_string_1, k_value_1)
    print(f"Unique substrings of length {k_value_1} in '{test_string_1}':")
    for sub in result_1:
        print(sub)

    result_2 = extractor.get_unique_substrings(test_string_2, k_value_2)
    print(f"\nUnique substrings of length {k_value_2} in '{test_string_2}':")
    for sub in result_2:
        print(sub)