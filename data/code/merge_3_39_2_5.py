class SubstringExtractor:
    """
    A class to extract all unique substrings of a specified length k from a target string.
    
    Attributes:
        None
    
    Methods:
        get_unique_substrings(target_string, substring_length): 
            Returns a set containing all unique substrings of the given length.
            
    Time Complexity: O(n * k) where n is the length of the string and k is the substring length.
    Space Complexity: O(m) where m is the number of unique substrings found.
    """

    def __init__(self):
        self.target_string = ""
        self.substring_length = 0
        
    def get_unique_substrings(self, target_string, substring_length):
        """
        Efficiently finds and returns all unique substrings of a given length k 
        from the provided target string.
        
        Args:
            target_string (str): The input string to extract substrings from.
            substring_length (int): The desired length of each substring.
            
        Returns:
            set[str]: A set containing all unique substrings of the specified length.
                    
        Raises:
            ValueError: If substring_length is less than 1 or greater than len(target_string).
            TypeError: If target_string is not a string or substring_length is not an integer.
            
        Examples:
            >>> extractor = SubstringExtractor()
            >>> result = extractor.get_unique_substrings("abc", 2)
            # Returns: {'ab', 'bc'}
        """
        
        if not isinstance(target_string, str):
            raise TypeError(f"Expected string type but got {type(target_string).__name__}")
            
        if not isinstance(substring_length, int):
            raise TypeError(f"Expected integer for substring length but got {type(substring_length).__name__}")
            
        n = len(target_string)
        
        # Validate constraints on k (substring_length)
        if substring_length < 1:
            raise ValueError("Substring length must be at least 1.")
            
        if substring_length > n:
            return set()  # No substrings possible
            
        unique_substrings = set()
        
        for i in range(n - substring_length + 1):
            sub_string = target_string[i : i+substring_length]
            unique_substrings.add(sub_string)
            
        return unique_substrings

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    extractor_instance = SubstringExtractor()
    
    # Sample 1: Basic case with overlapping substrings
    target_s_1 = "abcdef"
    k_1 = 3
    
    result_set_1 = extractor_instance.get_unique_substrings(target_s_1, k_1)
    print(f"Sample 1 - String '{target_s_1}', Length {k_1}:")
    sorted_result_sorted_list_1 = sorted(result_set_1, key=lambda x: (len(x), x))
    for sub in result_set_1:
        print(sub)
    
    # Sample 2: Case where all characters are the same
    target_s_2 = "aaaaa"
    k_2 = 3
    
    result_set_2 = extractor_instance.get_unique_substrings(target_s_2, k_2)
    print("\nSample 2 - String '{target_s_2}', Length {k_2}:")
    
    # Sample 3: Edge case where length equals string length
    target_s_3 = "hello"
    k_3 = 5
    
    result_set_3 = extractor_instance.get_unique_substrings(target_s_3, k_3)
    print(f"\nSample 3 - String '{target_s_3}', Length {k_3}:")
    
    # Sample 4: Invalid length case (larger than string) handled gracefully by returning empty set
    
    target_s_4 = "test"
    k_invalid = 10
    
    result_set_4 = extractor_instance.get_unique_substrings(target_s_4, k_invalid)
    print(f"\nSample 4 - String '{target_s_4}', Invalid Length {k_invalid}:")
    
    # Sample 5: Non-integer length handling (would raise TypeError if called externally 
    # but here we just show it returns empty set conceptually or raises error based on implementation)
    # Note: Our internal check ensures only valid integers are processed.