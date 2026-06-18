class StringExtractor:
    """A class to extract non-overlapping substrings based on delimiter positions."""
    
    def __init__(self, delimiters):
        """
        Initialize the extractor with a list of integer indices representing 
        the start and end positions (exclusive) for each substring.

        Args:
            delimiters (list[int]): A flat list where even-indexed elements are starts
                                   and odd-indexed elements are ends for each segment.
                                     Example: [0, 3, 5, 9] -> "abc" at 0-3, "defgh" at 5-9
        """
        if len(delimiters) % 2 != 0 or any(i < j and i >= delimiters[j//2 + 1] for i, j in enumerate(range(0, len(delimiters), 2))):
            raise ValueError("Delimiters must be a list of pairs (start, end) where start < end.")

        self.segments = []
        if not delimiters:
            return
        
        # Process and validate segments first to ensure logical ordering for non-overlapping extraction logic later if needed.
        # Although the prompt implies simple slicing based on provided positions, 
        # we assume valid input per spec (start < end).
        
    def extract(self, text):
        """
        Extract all substrings from the given text using the stored delimiter pairs.

        Args:
            text (str): The source string to extract substrings from.

        Returns:
            list[str]: A list of extracted non-overlapping substring strings.
        
        Raises:
            IndexError: If a segment's end index is out of bounds for the given text length.
        """
        if len(self.segments) == 0:
            return []

        results = []
        
        # Ensure segments are ordered to prevent overlap logic issues, 
        # though typically provided positions might be unordered.
        sorted_segments = sorted(zip(range(1, -1, -2), self.segments)) 
        
        for i in range(len(self.segments)):
            start_idx = self.segments[i][0]
            end_idx = self.segments[i][1]

            if not (isinstance(start_idx, int) and isinstance(end_idx, int) 
                   and 0 <= start_idx < len(text) and 0 <= end_idx <= len(text)) or \
               start_idx > end_idx: # Allow empty strings but ensure valid bounds
            
                continue
                
        segments = []

    def _process_segments(self):
        """Helper to process the raw list into a clean structure."""
        processed = []

if __name__ == '__main__':
    pass
