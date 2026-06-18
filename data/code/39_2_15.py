class SubstringExtractor:
    def __init__(self):
        self.substrings = set()  # Using a set to ensure uniqueness efficiently
    
    def extract_substrings(self, target_string, k):
        """
        Finds and returns all unique substrings of length k from the target string.
        
        Args:
            target_string (str): The input string to analyze.
            k (int): The desired length of the substrings.
            
        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
        """
        if not isinstance(target_string, str) or not isinstance(k, int):
            raise TypeError("Input arguments must be a string and an integer.")
        
        n = len(target_string)
        
        # If the requested substring length is greater than the string length, return empty list
        if k <= 0 or k > n:
            return []
        
        seen_substrings = set()
        result_list = []
        
        for i in range(n - k + 1):
            sub_string = target_string[i:i+k]
            
            # Add to the global unique set immediately upon finding it
            self.substrings.add(sub_string)
            result_list.append(sub_string)
        
        return sorted(self.substrings, key=lambda x: (len(x), x))

if __name__ == '__main__':
    extractor = SubstringExtractor()
    
    # Sample values - no user input required
    target_str = "abcdefg"
    k_length = 3
    
    unique_subs = extractor.extract_substrings(target_str, k_length)
    
    print(f"Unique substrings of length {k_length} from '{target_str}':")
    for sub in unique_subs:
        print(sub)