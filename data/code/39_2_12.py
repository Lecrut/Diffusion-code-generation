class SubstringExtractor:
    def __init__(self):
        pass
    
    def get_unique_substrings(self, target_string: str, k: int) -> set:
        """
        Efficiently finds and returns all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to search within.
            k (int): Length of the substring.
            
        Returns:
            set[str]: A set containing unique substrings of length k.
            
        Raises:
            ValueError: If k is not a positive integer or greater than the string length plus one.
            IndexError: If k is larger than the available characters in the target_string minus one (to form at least one substring).
        """
        if not isinstance(k, int) or k <= 0:
            raise ValueError("Length 'k' must be a positive integer.")
        
        string_length = len(target_string)
        
        # Ensure that it's possible to extract at least one substring of length k.
        # A valid start index goes from 0 up to (string_length - k). So max_start is int(math.floor(string_length - k)). 
        # If no such integer exists, raise an error.
        if string_length < k:
            raise IndexError(f"String length ({string_length}) is less than required substring length ({k}).")

        unique_substrings = set()
        
        start_index = 0
        while True:
            end_index = start_index + k
            
            # If we exceed the boundaries of the string, stop. We need at least one full chunk of size k ending before or at len(s). 
            # Actually simpler logic: if start_index > length - k, no more substrings possible.
            if start_index >= string_length - k + 1:
                break
                
            substring = target_string[start_index : end_index]
            
            unique_substrings.add(substring)
            
            start_index += 1
            
        return unique_substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()

    # Sample test case 1: General string
    sample_str_1 = "abracadabra"
    k_value_1 = 3
    
    result_1 = extractor.get_unique_substrings(sample_str_1, k_value_1)
    
    print(f"Unique substrings of length {k_value_1} in '{sample_str_1}':")
    for s in sorted(result_1):
        print(s)

    # Sample test case 2: Identical string repetition to verify uniqueness filtering
    sample_str_2 = "banana"
    k_value_2 = 3
    
    result_2 = extractor.get_unique_substrings(sample_str_2, k_value_2)
    
    print(f"\nUnique substrings of length {k_value_2} in '{sample_str_2}':")
    for s in sorted(result_2):
        print(s)

    # Sample test case 3: Edge case - exactly one possible substring
    sample_str_3 = "hello"
    k_value_3 = 5
    
    result_3 = extractor.get_unique_substrings(sample_str_3, k_value_3)
    
    print(f"\nUnique substrings of length {k_value_3} in '{sample_str_3}':")
    for s in sorted(result_3):
        print(s)

    # Sample test case 4: Error handling check (k > string_length, expected to raise IndexError inside function call logic if triggered by input change, but here static values used). 
    # Note: We won't trigger the error with current hard-coded samples as they are valid.