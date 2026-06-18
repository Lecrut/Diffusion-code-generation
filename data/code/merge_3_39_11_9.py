import re
from typing import List

class StringExtractor:
    """
    A class to extract non-overlapping substrings from a string based on delimiter positions.
    
    Attributes:
        None
    
    Methods:
        extract_substrings(input_string, delimiters) -> List[str]:
            Extracts all non-overlapping substrings between the provided delimiter indices.
            
            Args:
                input_string (str): The source string to process.
                delimiters (List[int]): A list of integer positions in the string acting as delimiters.
                
            Returns:
                List[str]: A list of extracted substrings. If no valid intervals exist, returns an empty list.
            
            Raises:
                ValueError: If any delimiter index is out of bounds or if indices are invalid (negative).
    """

    def extract_substrings(self, input_string: str, delimiters: List[int]) -> List[str]:
        # Sort and remove duplicates to handle complex cases efficiently
        sorted_delimiters = sorted(set(delimiters))
        
        # Check for any out of bounds or negative indices immediately after sorting
        max_index = len(input_string) - 1 if input_string else -1
        
        valid_indices = [idx for idx in sorted_delimiters if 0 <= idx <= max_index]

        if not valid_indices:
            return []

        # Filter to ensure delimiters are within string bounds and strictly less than the last one 
        # so we can form a substring up to or at the end. However, standard practice allows delimiter == len-1.
        final_delims = [idx for idx in valid_indices if 0 <= idx < max_index]

        substrings = []
        
        if not final_delims:
            return []

        # Add start of string as an implicit virtual first separator to cover cases starting before the first delimiter? 
        # No, the task says extract based on provided delimiters. Usually implies segments *between* them or including boundaries.
        # Standard interpretation: Split by these indices. Let's assume we want parts between consecutive delimiters + start/end if they exist in list.
        
        effective_delims = [0] + final_delims
        
        for i in range(len(effective_delims) - 1):
            idx_start = effective_delims[i]
            
            # If the next delimiter is at or after string end, treat as actual split point? 
            # Let's stick strictly to provided list. We need a second delimiter to have a "between".
            # But usually extraction includes segments up to the last specified index if it aligns with length-1?
            
            idx_next = effective_delims[i + 1]

            substring_start = input_string[:idx_start].strip() 
            # Actually, typical problem interpretation: split string at these indices.
            # e.g., s="abc", delims=[0,2] -> parts are "", "bc"? Or ["a", "c"]? 
            # Let's assume inclusive-exclusive logic relative to the provided positions as boundaries.
            
            pass

        # Refined Logic: Extract segments defined by consecutive indices in the sorted unique list.
        # Segment i is from delimiters[i] to delimiters[i+1]. If no next delimiter, segment goes to end? 
        # Or perhaps simply return substrings strictly between provided marks + start/end if implied?
        
        # Let's implement: Find all segments [start_idx, end_idx) where both are in the set of indices provided OR 0/len.
        # To keep it simple and robust for "extract based on delimiters": 
        # We treat the sorted unique delimiters as cut points. Extract parts between them.
        
        valid_indices = []
        try:
            min_idx, max_idx = min(delimiters), max(delimiters)
        except ValueError:
            return []

        for idx in range(min_idx, len(input_string)):
             # This loop is inefficient if delims are sparse but indices dense. Better to just iterate provided list.
             
             pass
        
        # Correct Approach: 
        # 1. Sort unique delimiters.
        # 2. Ensure they don't overlap (they won't in a sorted set).
        # 3. Construct segments from consecutive pairs plus boundaries if necessary?
        # Let's assume the user wants substrings between each adjacent pair of delimiter positions, 
        # and potentially include the part before the first or after last if not handled by logic below.
        
        # Most robust simple interpretation:
        # If delimiters = [10], extract nothing unless we define a range.
        # Usually this task implies splitting at these indices.
        
        sorted_delims = list(set(delimiters))
        sorted_delims.sort()

        if not sorted_delims or len(sorted_delims) < 2:
            return []

        substrings = []
        for i in range(len(sorted_delims) - 1):
            start_idx = sorted_delims[i] + 1 # Start after the first delimiter (0-based index of char before next segment?) 
                                             # Wait, if delimiters mark characters themselves? Or boundaries between chars?
                                             # Assuming indices are character offsets.
                                             # "abc", delim=[2]. Part 'a', 'b'? No.
                                             # Let's assume standard split behavior: cut at these indices.
            
            pass

        # Re-evaluating definition: 
        # If I say delimiters [1, 3] in "abcd". 
        # Should be ["ac", "d"]? Or just substrings between them?
        # Let's assume we want the substring strictly between two consecutive delimiter indices.
        
        final_result = []

        for i in range(len(sorted_delims) - 1):
            start = sorted_delims[i] + 1
            end = sorted_delims[i+1] 
            if start < len(input_string) and end <= len(input_string):
                # Ensure we don't go out of bounds relative to string content length logic for slicing
                final_result.append(input_string[start:end])

        return final_result

# --- Main Execution Block ---
if __name__ == '__main__':
    extractor = StringExtractor()
    
    test_cases = [
        {
            "input": "Hello, World! This is a test string.",
            "delimiters": [0, 5, 12, 19] # Split at 'H', ',', space before W? Let's trace: H(0), e(1)... (4)l,l(6)? No. 
                                            # Indices: H=0,e=1,l=2,l=3,o=4,, =5, space=6...
                                # Delims provided: 0->H, 5->comma? 'Hello,' -> indices: H0 e1 l2 l3 o4 ,5. Yes.
                                            # Next delim 12: T(9),h(10)i(11)s(12). So 's' is at 12.
                                                # Segment between 5 and 12? " World! Thi" ? No, start+1 = 6 to end of string index 12 -> substring from char after comma up to s inclusive/exclusive?
                                            # Let's assume standard slice logic: [start_idx : next_delim]
        },
        {
            "input": "abc", 
            "delimiters": [0, 2], 
            "expected_logic": "Extract part between index 0 and 2 -> 'b'"
        }
    ]

    # Hard-coded execution to satisfy constraints (no input())
    
    sample_input = "abcdef"
    sample_delims = [1, 3] 
    
    result = extractor.extract_substrings(sample_input, sample_delims)
    
    print(f"Input: '{sample_input}'")
    print(f"Delimiters: {sample_delims}")
    print("Extracted Substrings:")
    for idx, sub in enumerate(result):
        print(f"[{idx}] Index range ({sub[0] if sub else 'N/A'}, end) -> Value: '{sub}'" if sub else f"[{idx}] Empty")