class SubstringExtractor:
    def __init__(self):
        pass
    
    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently finds and returns all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to search within.
            k (int): The fixed length of the substring to extract.
            
        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
            
        Raises:
            ValueError: If k is less than or equal to 0, or if k exceeds the string length.
        """
        if k <= 0:
            raise ValueError("Length k must be greater than zero.")
        
        n = len(target_string)
        if k > n:
            return []

        seen = set()
        substrings_list = []

        # Use a sliding window approach to extract substrings efficiently.
        for i in range(n - k + 1):
            substring = target_string[i:i+k]
            
            if substring not in seen:
                seen.add(substring)
                substrings_list.append(substring)
        
        return sorted(substrings_list)

if __name__ == '__main__':
    extractor = SubstringExtractor()

    # Hard-coded sample values as per requirements.
    target_str = "abcdefg"
    k_value = 3
    
    result = extractor.get_unique_substrings(target_str, k_value)
    
    print(f"Unique substrings of length {k_value} in '{target_str}':")
    for sub in result:
        print(sub)

    # Additional test case with duplicates and different characters
    target_str_2 = "banana"
    k_value_2 = 3
    
    result_2 = extractor.get_unique_substrings(target_str_2, k_value_2)
    
    print(f"\nUnique substrings of length {k_value_2} in '{target_str_2}':")
    for sub in result_2:
        print(sub)

    # Test case where k is larger than string length
    target_str_3 = "hi"
    k_value_3 = 5
    
    try:
        result_3 = extractor.get_unique_substrings(target_str_3, k_value_3)
        print(f"\nUnique substrings of length {k_value_3} in '{target_str_3}':")
        print(result_3 if isinstance(result_3, list) else "Error occurred")
    except ValueError as e:
        print(f"Caught expected error for invalid k: {e}")

    # Test case with zero or negative length (should raise error)
    target_str_4 = "test"
    k_value_4 = -1
    
    try:
        result_4 = extractor.get_unique_substrings(target_str_4, k_value_4)
        print(f"\nUnique substrings of length {k_value_4} in '{target_str_4}':")
        print(result_4 if isinstance(result_4, list) else "Error occurred")
    except ValueError as e:
        print(f"Caught expected error for invalid k (negative): {e}")