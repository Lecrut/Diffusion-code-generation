import sys

class StringExtractor:
    def __init__(self):
        """Initialize the StringExtractor class."""
        pass

    def extract_substrings(self, input_string: str, delimiter_positions: list[int]) -> list[str]:
        """
        Extract all non-overlapping substrings from a given input string 
        based on provided delimiter positions.

        Args:
            input_string (str): The source string to process.
            delimiter_positions (list[int]): List of integer indices where delimiters occur.

        Returns:
            list[str]: A list of extracted non-overlapping substrings between consecutive delimiters.
        
        Note:
            - Delimiter positions are 0-based indices in the input_string.
            - Substrings include characters strictly between two adjacent delimiter positions.
            - If no valid substring exists (e.g., fewer than 2 delimiters), an empty list is returned.
            - Positions must be within bounds [0, len(input_string)).
        """
        if not isinstance(delimiter_positions, list) or not all(isinstance(x, int) for x in delimiter_positions):
            raise TypeError("delimiter_positions must be a list of integers.")

        n = len(input_string)
        
        # Filter and sort unique valid positions within bounds
        sorted_delims = []
        seen = set()
        for pos in delimiter_positions:
            if 0 <= pos < n and pos not in seen:
                sorted_delims.append(pos)
                seen.add(pos)

        # Sort to ensure order (though input might be unsorted, we want consistent behavior)
        sorted_delims.sort()

        substrings = []

        # If less than 2 delimiters, no substring can exist between them
        if len(sorted_delims) < 2:
            return substrings

        for i in range(len(sorted_delims) - 1):
            start_idx = sorted_delims[i] + 1
            end_idx = sorted_delims[i+1]
            
            # Ensure we don't go out of bounds or capture empty strings if adjacent indices are used directly without char gap logic? 
            # Actually, the substring is from (pos_i + 1) to pos_{i+1} inclusive/exclusive depending on definition.
            # Typically "between" means exclusive of delimiters themselves.
            # So slice: input_string[start_idx:end_idx] where end_idx is the next delimiter index itself? 
            # Let's define substring as characters strictly between two consecutive delimiters.
            
            if start_idx < n and end_idx > 0:
                substrings.append(input_string[start_idx:end_idx])

        return substrings

if __name__ == '__main__':
    extractor = StringExtractor()
    
    # Hard-coded sample values as per requirements (no user input, no args)
    test_input_str = "Hello-World@Test"
    delimiter_positions_list = [5, 10]

    result_substrings = extractor.extract_substrings(test_input_str, delimiter_positions_list)

    print("Input String:", repr(test_input_str))
    print("Delimiter Positions:", delimiter_positions_list)
    print("Extracted Substrings:")
    for idx, sub in enumerate(result_substrings):
        print(f"  [{idx}]: {repr(sub)}")