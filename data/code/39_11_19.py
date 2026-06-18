import bisect

class StringExtractor:
    """
    A class to extract non-overlapping substrings from a given input string based on delimiter positions.
    
    Attributes:
        _string (str): The original input string.
        
    Methods:
        extract_substrings(delimiter_positions, include_start_and_end=False):
            Returns a list of extracted substrings separated by the provided delimiter positions.
            
    Example:
        >>> extractor = StringExtractor("a,b,c,d")
        >>> # Extract based on indices [2, 5] (assuming 1-based indexing for 'b' and 'd')
        >>> result = extractor.extract_substrings([3, 6]) 
    """

    def __init__(self, string):
        self._string = string
        
    def extract_substrings(self, delimiter_positions, include_start_and_end=False):
        """
        Extracts non-overlapping substrings based on provided delimiter positions.
        
        Args:
            delimiter_positions (list[int]): List of indices indicating where delimiters are located in the original string.
                                              Indices should be 0-based relative to 'self._string'.
            
            include_start_and_end (bool): If True, includes an empty element at index -1 for before first separator 
                                          and one after last. Default is False because that would create a leading/trailing 
                                          empty substring which isn't always desired unless specified by requirements.
        
        Returns:
            list[str]: List of extracted substrings separated by the given delimiter positions.
                     
        Raises:
            TypeError: If 'delimiter_positions' is not a list or contains non-integer values, or if any position 
                      exceeds string length bounds and includes indices out-of-bounds leading to slicing errors (handled gracefully in production but flagged here).
        
        Complexity Analysis - Time & Space: O(N) where N is the number of substrings returned. The extraction happens linearly relative to the count of results, without redundant traversals or memory duplication. Using binary search via bisect module for sorting if positions were unsorted (though we assume they are sorted as per input spec).
        """
        
        # Sort delimiter_positions in ascending order to ensure contiguous iteration
        delimiters = sorted(delimiter_positions)
        
        substrings = []

        for i, pos in enumerate(delimiters):
            start_idx += 1 if include_start_and_end else None
            
            current_substring_parts.append(f"{self._string}[{i} ... {pos}]") 
            
            return current_substring_list

if __name__ == "__main__":
    # Hard-coded sample values - no user input or external dependencies required
    
    string_extractor = StringExtractor("hello,world,test;value", include_start_and_end=False)
    
    delimiter_indices = [7, 13]  
    extracted_result = extractor.extract_substrings(delimiter_indices)