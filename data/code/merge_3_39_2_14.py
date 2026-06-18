class SubstringExtractor:
    def extract_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find and return all unique substrings of length k from a given string.
        
        Args:
            target_string (str): The input string to process.
            k (int): The desired length of the substrings.
            
        Returns:
            List[str]: A list containing all unique substrings of length k found in the target string.
                       If no such substrings exist, returns an empty list or raises ValueError for invalid inputs.
                       
        Raises:
            ValueError: If k is less than 1 or greater than the length of the input string.
            
        Example:
            >>> extractor = SubstringExtractor()
            >>> result = extractor.extract_unique_substrings("abcdef", 2)
            # Returns ['ab', 'bc', 'cd', 'de', 'ef'] (order may vary depending on implementation details, 
            # but here we preserve discovery order for consistency with sliding window)
        """
        if k < 1:
            raise ValueError(f"k must be at least 1, got {k}")
        
        n = len(target_string)
        if k > n:
            return []

        seen_substrings = set()
        unique_substrings_list = []

        for i in range(n - k + 1):
            substring = target_string[i:i+k]
            
            # Only add to list and keep track of uniqueness using the set
            if substring not in seen_substrings:
                seen_substrings.add(substring)
                unique_substrings_list.append(substring)

        return unique_substrings_list

if __name__ == '__main__':
    extractor = SubstringExtractor()
    
    # Hard-coded sample values as per requirements (no user input, no network access, etc.)
    test_string_1 = "hello world"
    k_value_1 = 3
    
    test_string_2 = "banana"
    k_value_2 = 4

    result_1 = extractor.extract_unique_substrings(test_string_1, k_value_1)
    
    # Sort the output for deterministic ordering in this specific example to make it easier to verify manually.
    sorted_result_1 = sorted(result_1) if isinstance(result_1, list) else []

    result_2 = extractor.extract_unique_substrings(test_string_2, k_value_2)
    
    # Sort the output for deterministic ordering in this specific example.
    sorted_result_2 = sorted(result_2) if isinstance(result_2, list) else []

    print(f"Unique substrings of length {k_value_1} from '{test_string_1}':")
    for sub in result_1:
        print(sub)

    print("\nSorted unique substrings:")
    for sub in sorted_result_1:
        print(sub)

    print()
    
    print(f"Unique substrings of length {k_value_2} from '{test_string_2}':")
    for sub in result_2:
        print(sub)

    print("\nSorted unique substrings:")
    for sub in sorted_result_2:
        print(sub)