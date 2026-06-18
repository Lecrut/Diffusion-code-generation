class SubstringExtractor:
    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find all unique substrings of length k from a given string.

        Args:
            target_string (str): The input string to extract substrings from.
            k (int): The desired length of the substrings.

        Returns:
            List[str]: A list containing all unique substrings of length k found in the 
                      target_string, preserving the order of first occurrence.
        
        Raises:
            ValueError: If k is less than 1 or greater than the length of the string.
        """
        if k < 1:
            raise ValueError("Length k must be at least 1.")
        if k > len(target_string):
            return []

        unique_substrings = set()
        result_list = []

        for i in range(len(target_string) - k + 1):
            substring = target_string[i : i + k]
            if substring not in unique_substrings:
                unique_substrings.add(substring)
                result_list.append(substring)

        return result_list

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    extractor = SubstringExtractor()
    
    test_string_1 = "abcdef"
    k_value_1 = 2
    
    print(f"\nTest Case 1:")
    print(f"Input String: {test_string_1}")
    print(f"Length K: {k_value_1}")
    substrings_result_1 = extractor.get_unique_substrings(test_string_1, k_value_1)
    for sub in substrings_result_1:
        print(sub)
    
    test_string_2 = "banana"
    k_value_2 = 3
    
    print(f"\nTest Case 2:")
    print(f"Input String: {test_string_2}")
    print(f"Length K: {k_value_2}")
    substrings_result_2 = extractor.get_unique_substrings(test_string_2, k_value_2)
    for sub in substrings_result_2:
        print(sub)
    
    test_string_3 = "aaa"
    k_value_3 = 1
    
    print(f"\nTest Case 3:")
    print(f"Input String: {test_string_3}")
    print(f"Length K: {k_value_3}")
    substrings_result_3 = extractor.get_unique_substrings(test_string_3, k_value_3)
    for sub in substrings_result_3:
        print(sub)