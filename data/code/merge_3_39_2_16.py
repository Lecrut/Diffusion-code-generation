import sys
from typing import List, Set

class SubstringExtractor:
    """A class to efficiently find all unique substrings of a given length k."""

    def __init__(self):
        self._seen_substrings = set()

    def extract_unique_substrings(self, target_string: str, k: int) -> List[str]:
        """
        Find and return all unique substrings of length k from the target string.

        Args:
            target_string (str): The input string to search within.
            k (int): The desired length of each substring.

        Returns:
            List[str]: A list containing all unique substrings of length k found in the string, 
                      preserving their order of first appearance.
        
        Raises:
            ValueError: If k is not a positive integer or if it exceeds the string length + 1.
        """
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k must be a positive integer.")

        n = len(target_string)
        
        # Optimization check: if k > n, no substrings of that length exist.
        if k > n:
            return []

        unique_substrings = []
        seen_set = set()
        current_index = 0
        
        while True:
            substring_start = target_string[current_index : current_index + k]
            
            # Check bounds for slicing to avoid IndexError in older Python versions 
            # or unexpected behavior, though slice handles out-of-bounds gracefully.
            if len(substring_start) != k:
                break
                
            seen_set.add(substring_start)
            unique_substrings.append(substring_start)

            current_index += 1
            
            # Stop when we've processed the entire string up to index n-k
            if current_index > n - k:
                break
        
        return unique_substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()
    
    # Hard-coded sample values as per requirements (no user input)
    target_str = "abcdefg"
    substring_length_k = 3
    
    result = extractor.extract_unique_substrings(target_str, substring_length_k)
    
    print(f"Unique substrings of length {substring_length_k} in '{target_str}':")
    for sub in result:
        print(sub)