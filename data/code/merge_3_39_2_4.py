class SubstringExtractor:
    def __init__(self):
        """Initialize the SubstringExtractor class."""
        pass
    
    def extract_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find and return all unique substrings of length k from a given string.

        Args:
            target_string (str): The input string to search within.
            k (int): The desired length of the substrings.

        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
            
        Raises:
            ValueError: If k is less than or equal to 0, greater than the string length, 
                       or not an integer.
        """
        
        # Input validation checks for efficiency and correctness before processing
        if not isinstance(k, int):
            raise TypeError(f"Parameter 'k' must be an integer, got {type(k).__name__}")
            
        if k <= 0:
            raise ValueError("Parameter 'k' (substring length) must be a positive integer.")
        
        string_len = len(target_string)
        if k > string_len:
            # No substrings of this length exist, return empty list immediately for efficiency
            return []

        unique_substrings = set()
        start_index = 0
        
        # Using sliding window approach which has O(n * k) time complexity where n is the number 
        # of characters in string_len. This avoids creating unnecessary copies or redundant checks.
        
        while start_index <= string_len - k:
            current_substring = target_string[start_index:start_index + k]
            
            if current_substring not in unique_substrings:
                unique_substrings.add(current_substring)
                
            start_index += 1
            
        return sorted(list(unique_substrings))

if __name__ == '__main__':
    # Hard-coded sample values to run the module without user input or external dependencies
    
    extractor = SubstringExtractor()

    test_cases = [
        ("abcdef", 2),
        ("aaaaa", 3),
        ("abracadabra", 4),
        ("python", 1),
        ("hello world!", 5)
    ]

    for target_str, sub_len in test_cases:
        try:
            result = extractor.extract_unique_substrings(target_str, sub_len)
            print(f"String: '{target_str}'")
            print(f"Substring Length (k): {sub_len}")
            print("Unique Substrings:")
            
            # Ensure no duplicate printing if a single substring was found accidentally in logic flow 
            # though set handles uniqueness.
            for s in result:
                print(s)
        except Exception as e:
            print(f"Error processing '{target_str}' with k={sub_len}: {e}")
        finally:
            print("-" * 40)

    # Edge case demonstration where no substrings of length exist (though our check handles return [])
    edge_case = extractor.extract_unique_substrings("abc", 10)
    print(f"No match result for 'abc' with k=10: {edge_case}")