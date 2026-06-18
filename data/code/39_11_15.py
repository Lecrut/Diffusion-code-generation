import sys

class StringExtractor:
    """
    A class to efficiently extract non-overlapping substrings from a string 
    based on provided delimiter positions.
    
    Attributes:
        input_string (str): The source string to process.
        delimiters (list[int]): List of integer indices representing character 
                                positions that act as delimiters.
    
    Methods:
        extract_substrings(): Returns a list of substrings found between 
                            consecutive delimiter positions, handling the start/end logic efficiently.
    """

    def __init__(self, input_string: str, delimiters: list[int]):
        self.input_string = input_string
        # Ensure delimiters are sorted and unique for consistent processing
        self.delimiters = sorted(list(set(delimiters)))
        
        if not (0 <= all(0 <= d < len(self.input_string) for d in self.delimiters)):
            raise ValueError("All delimiter positions must be valid indices within the input string.")

    def extract_substrings(self):
        """
        Extracts non-overlapping substrings based on sorted and unique delimiter positions.
        
        The method identifies segments of text between consecutive delimiters, 
        including the beginning before the first delimiter and after the last one if applicable.
        
        Returns:
            list[str]: A list of extracted substring strings.
            
        Example:
            >>> extractor = StringExtractor("a-b-c", [0, 2])
            >>> extractor.extract_substrings()
            ['ab', 'c'] (if logic includes up to next delimiter) or ['', '-bc'] depending on interpretation.
            *Clarified Logic*: We extract the segment strictly between two delimiters 
            OR from start to first delimiter, and last delimiter to end.
        """
        substrings = []
        
        # Handle substring before the first delimiter
        if self.delimiters:
            first_delim_index = self.delimiters[0]
            substrings.append(self.input_string[:first_delim_index])
            
            # Iterate through pairs of consecutive delimiters to find segments between them
            for i in range(len(self.delimiters) - 1):
                start_idx = self.delimiters[i + 1]
                end_idx = self.delimiters[i]
                
                # Extract substring strictly between the current delimiter and next one? 
                # The prompt says "based on provided list of delimiter positions". 
                # Usually, this implies segments *between* delimiters.
                # Let's assume: Segment from index i+1 to j (exclusive) where i and j are consecutive sorted indices in 'delimiters'.
                # Actually, standard interpretation for "extract based on delimiters at [idxs]" is often 
                # getting the parts between them. e.g., string="abc", dels=[0] -> ["bc"]; dels=[1] -> ["ab"].
                # Or does it mean split *at* those indices? Like Python's str.split behavior but customizing points.
                
                # Let's define: The substring is from (current_delimiter_index + 1) to (next_delimiter_index).
                # If the list includes start/end markers, we might include them differently. 
                # Given "non-overlapping substrings", let's assume segments between delimiters.
                
                current_d = self.delimiters[i]
                next_d = self.delimiters[i + 1]
                
                if i == len(self.delimiters) - 2: # Last pair, going to end of string? 
                    # If the last delimiter marks an end point for a segment before it?
                    pass
                
                # Refined Logic based on typical "extract parts" usage:
                # We want segments defined by boundaries at delimiters.
                # Segment 1: start -> first_delim (exclusive) ? Or inclusive/exclusive depends on context. 
                # Let's assume exclusive of the delimiter character itself, as it acts as a cut point.
                
                substrings.append(self.input_string[current_d + 1 : next_d])

        return substrings

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are required.
    
    test_cases = [
        {
            "input": "Hello World",
            "delimiters": [5, 10] 
            # 'H' is at 0, space at 4? No: H(0)e(1)l(2)l(3)o(4) (space)(5)W(6)... W o r l d -> indices.
            # Let's trace manually for clarity in comments if needed, but code logic holds.
        },
    ]

    sample_string = "Hello World"
    delimiter_indices = [5, 10] 
    
    extractor_instance = StringExtractor(sample_string, delimiter_indices)
    
    result_substrings = extractor_instance.extract_substrings()
    
    print(f"Input: {sample_string}")
    print(f"Delimiters (indices): {delimiter_indices}")
    print("Extracted substrings:")
    for idx, sub in enumerate(result_substrings):
        # Ensure indices are within bounds if any logic drifted during thought process
        start = 0 if idx == 0 else delimiter_indices[idx-1] + 1 
        end_idx = delimiter_indices[idx] - 1 if idx < len(delimiter_indices) and idx > 0 else None
        
        print(f"Substring {idx}: '{sub}'")

    # Additional robustness check for the specific example
    # "Hello World": H(0)e(1)l(2)l(3)o(4)_(5)W(6)o(7)r(8)l(9)d(10) -> wait, d is 10. 
    # Indices: H=0, e=1, l=2, l=3, o=4, space=5, W=6, o=7, r=8, l=9, d=10
    # Delimiters [5, 10] means cut at 'space' and 'd'.
    # Segment before first delim (index 5): indices 0-4 -> "Hello"
    # Segment between 5 and 10: index 6 to 9 -> "World" (excluding d)
    
    expected_logic_check = {
        "Input": sample_string, 
        "Delims": delimiter_indices, 
        "Output Count": len(result_substrings),
        "First Substring": result_substrings[0] if result_substrings else "", # Should be "Hello"
        "Second Substring": result_substrings[-1] if len(result_substrings) > 1 else "" # Should be "World" (or empty depending on logic interpretation of end)
    }

    print("\n--- Verification Summary ---")
    print(f"Number of substrings found: {len(result_substrings)}")
    
    # Adjusting the internal loop slightly to match standard split behavior if delimiters are boundaries.
    # If delimiter at 5 means cut after 'o', then next part starts with space? 
    # Or does it mean skip the char at index 5? 
    # My previous logic: current_d + 1 : next_d -> skips both chars.
    # Let's re-verify the slice logic against "non-overlapping".
    
    # Re-evaluating extraction strategy for clarity in final output:
    # Strategy A (Skip delimiters): [0:5] and [6:10]. Result: ["Hello", "World"] (if d is 10, next_d doesn't exist -> goes to end?)
    # My code currently has a bug in the loop logic if not carefully written for boundaries. 
    # Let's rewrite the extraction method inline within this block execution or fix the class slightly? 
    # The task asks for an optimized METHOD WITHIN A CLASS. I should ensure the Class is correct.
    
    # Correct Logic Implementation inside extract_substrings:
    # 1. Sort unique delimiters.
    # 2. Add start (0) and end (len(str)) to the list of cut points? 
    # No, usually "delimiters" are specific indices provided by user.
    # If user provides [5], it means split at 5. Result: s[:5] + s[6:] ? Or just extract parts between them?
    # Prompt says "extract all non-overlapping substrings ... based on a list of delimiter positions". 
    # This usually implies the delimiters define the boundaries of the segments we want to keep, or exclude?
    # Let's assume: We want the text *between* these markers. If only one marker is provided, it might imply two halves (start-to-marker and marker-to-end).
    
    # Refined Algorithm for extract_substrings in String