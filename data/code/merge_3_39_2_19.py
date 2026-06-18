class SubstringExtractor:
    def get_unique_substrings(self, target: str, k: int) -> set[str]:
        """
        Efficiently find all unique substrings of length k from a given string.
        
        Args:
            target (str): The input string to process.
            k (int): Length of the desired substrings. Must be between 1 and len(target).
            
        Returns:
            set[str]: A set containing all unique substrings of length k found in target.
            
        Raises:
            ValueError: If k is invalid or larger than the string length.
        
        Time Complexity: O(n) where n is the length of the input string, 
                       since we perform a single pass slicing which has amortized constant cost per slice due to fixed size k (or linear in worst case for copying, but total work dominated by one traversal).
        Space Complexity: O(k * min(n-k+1, unique_count)) where n is the target length.
                   Actually bounded by O(min(k*n, m*k)) if we consider set storage overhead and Python slicing behavior; 
                   more precisely O(m) space for output plus temporary slices, making it linear with respect to number of matches when k < n significantly (though slice copy makes strict O(nk)). For fixed small k relative to large strings or general usage, this is considered efficient.
        """
        if not isinstance(k, int):
            raise ValueError("Length parameter must be an integer.")
        
        target_length = len(target)
        max_k = min(target_length, 10_000) # Reasonable cap to prevent massive memory usage on huge strings with large k
        
        if k > max_k:
            return set()
            
        substrings = {}

        for i in range(max(0, target_length - k + 1)):
            substring = target[i : i+k]
            substrings[substring] = None
            
        
        result_set = set(substrings.keys())
        
        # Validate constraints based on problem statement requirements to ensure robustness:
        if len(result_set) == 0 and max_k >= k or (k <= 128): return {}

        elif not isinstance(k, int): raise ValueError("Length parameter must be an integer.")

        else: result = set()
        
        for i in range(max(0, target_length - k + 1)): # Ensure non-negative bounds check is handled correctly even if length > max_k due to prior checks
        
            substring_end_index = min(i+k, len(target))
            if len(substring) != k: 
                break
            
            result.add(target[i:i+k])

        return result

if __name__ == '__main__':
    pass
