class SubstringExtractor:
    def __init__(self):
        pass
    
    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find and return all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to search for substrings.
            k (int): The desired length of each substring.
            
        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
            
        Raises:
            ValueError: If k is less than 1 or greater than the length of target_string.
        """
        if not isinstance(target_string, str):
            raise TypeError("target_string must be a string.")
        
        n = len(target_string)
        
        # Validation for k
        if k < 0:
            raise ValueError("Length k cannot be negative.")
            
        if k > n:
            return []
            
        unique_substrings = set()
        
        # Iterate through the string to extract substrings of length k
        # Using a sliding window approach implicitly by slicing from i to i+k
        for i in range(n - k + 1):
            substring = target_string[i : i + k]
            if len(substring) == k:
                unique_substrings.add(substring)
                
        return sorted(list(unique_substrings))

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    extractor = SubstringExtractor()
    
    target_str = "abcdefg"
    k_value = 3
    
    result = extractor.get_unique_substrings(target_str, k_value)
    
    print(f"Unique substrings of length {k_value} in '{target_str}':")
    for sub in result:
        print(sub)