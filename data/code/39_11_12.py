import itertools
from typing import List

class StringExtractor:
    """A class to efficiently extract non-overlapping substrings based on delimiter positions."""

    def __init__(self, input_string: str):
        """Initialize the extractor with an input string.

        Args:
            input_string (str): The source string from which substrings will be extracted.
        """
        self.input_string = input_string

    def extract_substrings(self, delimiter_positions: List[int]) -> List[str]:
        """Extract all non-overlapping substrings based on the provided list of delimiter positions.

        Delimiter positions are zero-based indices indicating where a substring should end (exclusive).
        The method sorts these positions to ensure correct ordering and handles edge cases like 
        out-of-order inputs or empty lists by returning an appropriate result set.

        Args:
            delimiter_positions (List[int]): A list of integer positions marking the start/end boundaries for substrings.

        Returns:
            List[str]: A list containing all extracted non-overlapping substrings in order.

        Raises:
            ValueError: If any position is negative or out of bounds relative to the input string length.
        """
        if not delimiter_positions:
            return []

        # Validate positions
        for pos in delimiter_positions:
            if pos < 0 or pos >= len(self.input_string):
                raise ValueError(f"Position {pos} is out of valid range (length={len(self.input_string)})")

        sorted_positions = sorted(delimiter_positions)

        substrings = []
        start_index = 0

        for end_index in sorted_positions:
            # Ensure we don't extract empty or duplicate segments if positions are adjacent duplicates
            if not self._is_valid_segment(start_index, end_index):
                continue
            
            substring = self.input_string[start_index:end_index]
            substrings.append(substring)
            
            start_index = end_index + 1

        # Handle the final segment from the last delimiter to the end of the string
        if start_index < len(self.input_string):
            final_substring = self.input_string[start_index:]
            substrings.append(final_substring)

        return substrings

    def _is_valid_segment(self, start: int, end: int) -> bool:
        """Check if a segment from start to end is valid (non-empty)."""
        return 0 <= start < end <= len(self.input_string)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No input(), sys.stdin, or arguments used.

    extractor = StringExtractor("Hello, World! This is a test.")

    # Sample delimiter positions: 
    # Indices after which substrings should end (exclusive).
    delimiters = [5, 10, 23] 

    result_substrings = extractor.extract_substrings(delimiters)

    print(f"Input String: {extractor.input_string}")
    print(f"Delimiter Positions: {delimiters}")
    print("Extracted Substrings:")
    
    for i, sub in enumerate(result_substrings):
        print(f"{i+1}. \"{sub}\"")