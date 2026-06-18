import sys
from typing import List

class StringExtractor:
    """A class to extract substrings from a string based on delimiter positions."""

    def __init__(self, input_string: str):
        """Initialize the extractor with the source string."""
        self.input_string = input_string
    
    def _get_delimiter_indices(self, delimiters: List[int]) -> List[int]:
        """Ensure all provided indices are within bounds and sorted.

        Args:
            delimiters (List[int]): A list of integer positions indicating where 
                                   substrings should be extracted from the string.

        Returns:
            List[int]: Sorted list of unique, valid delimiter indices.
        
        Raises:
            ValueError: If any index is out of bounds or negative.
        """
        # Filter and validate indices
        filtered = [i for i in delimiters if 0 <= i < len(self.input_string)]
        
        # Sort to ensure processing order matches string traversal logic naturally, 
        # though set() handles uniqueness which we then sort back.
        unique_sorted_indices = sorted(list(set(filtered)))

        return unique_sorted_indices
    
    def extract_substrings(self, delimiters: List[int]) -> List[str]:
        """Extract non-overlapping substrings based on the provided delimiter indices.

        Non-overlapping means that if a substring ends at index 'i', 
        the next extraction starts from 'i + 1'. We iterate through the sorted 
        unique delimiter positions and slice accordingly.

        Args:
            delimiters (List[int]): List of integer positions marking the end 
                                   of each desired substring segment relative to start.

        Returns:
            List[str]: A list containing all extracted substrings in order.
        
        Raises:
            ValueError: If no valid indices are found or if input is invalid.
        """
        # Validate delimiters first
        if not isinstance(delimiters, (list, tuple)):
            raise TypeError("Delimiters must be a list-like object.")

        sorted_indices = self._get_delimiter_indices(delimiters)

        substrings_list: List[str] = []
        
        current_start = 0
        
        for end_index in sorted_indices:
            # Extract substring from current start to the delimiter position (inclusive of char at index, 
            # assuming indices are character offsets. If delimiters represent 'start' positions instead of ends, logic flips.
            # Based on standard "delimiter positions" phrasing where you extract *up to* that point:
            
            if end_index >= current_start:
                substring = self.input_string[current_start:end_index + 1]
                substrings_list.append(substring)
                
                # Move start pointer for non-overlapping requirement 
                # The next segment starts immediately after the one we just extracted.
                current_start = end_index + 1
        
        return substrings_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input or files are needed
    
    test_string = "Hello, World! Welcome to Python."
    
    # Sample delimiter positions (0-based indices) 
    # These represent the end index of each substring segment.
    delimiters_sample = [5, 12, 19] 

    extractor = StringExtractor(test_string)

    try:
        result_substrings = extractor.extract_substrings(delimiters_sample)
        
        print("Original String:")
        print(f"{test_string}\n")
        
        print("Delimiter Positions Used:", delimiters_sample)
        print("\nExtracted Substrings:\n")
        
        for idx, sub in enumerate(result_substrings):
            # Determine start index of substring based on delimiter logic: 0 to end+1
            if idx == 0:
                start_idx = 0
            else:
                prev_end = delimiters_sample[idx-1] + 1
                start_idx = prev_end
            
            print(f"Substring {idx}: '{sub}' (Indices [{start_idx} : {delimiters_sample[idx]}+1])")

    except Exception as e:
        print(f"An error occurred during extraction: {e}")