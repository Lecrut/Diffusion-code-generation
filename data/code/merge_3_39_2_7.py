class SubstringExtractor:
    def __init__(self):
        pass
    
    def find_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently finds and returns all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to extract substrings from.
            k (int): The fixed length of each substring to be found.
            
        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
            
        Raises:
            ValueError: If k is not a positive integer or if the requested slice exceeds string bounds.
        """
        # Input validation based on constraints and logic requirements
        if not isinstance(k, int) or k <= 0:
            raise ValueError("Length k must be a positive integer.")
        
        n = len(target_string)
        max_valid_k = n - (k - 1)
        
        if k > max_valid_k:
            return []

        # Set to ensure uniqueness efficiently with O(1) average lookup time
        unique_substrings_set = set()
        
        # Efficient extraction using a sliding window approach concept, though Python slicing is already optimized.
        for i in range(n - k + 1):
            current_substring = target_string[i : i+k]
            unique_substrings_set.add(current_substring)
            
        return sorted(list(unique_substrings_set))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, argparse required args)
    extractor = SubstringExtractor()

    test_cases = [
        ("abcdef", 3),      # Expect: abc def ghi ... wait string is small. a bc cde def efg? no k=3 -> abcd... 
                           # "abc" indices 0,1; next is bcd at 1, etc.
    ]

    for target_str in ["abcdef", "aaaaaaa", "programming"]:
        try:
            result = extractor.find_unique_substrings(target_str, 2)
            print(f"String: '{target_str}', Length k=2")
            print(f"Unique substrings ({len(result)}): {result}")
            
            # Additional test with invalid input for demonstration (commented out logic to avoid crashing main if run externally without care? 
            # Actually, the prompt says no errors during sample execution ideally unless testing edge cases. 
            # Let's stick to valid k in samples).
        except ValueError as e:
            print(f"Error processing '{target_str}': {e}")

    # Specific test for duplicate characters handling
    result_dup = extractor.find_unique_substrings("ababa", 2)
    print("\nString: 'ababa', Length k=2")
    print(f"Unique substrings ({len(result_dup)}): {result_dup}")