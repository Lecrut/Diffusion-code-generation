def extract_substrings(text: str) -> list[str]:
    """Extract substrings defined by their start and end indices from a target string."""
    
    def validate_bounds(bounds):
        if not isinstance(bounds, (list, tuple)) or len(bounds) != 2:
            raise ValueError("Bounds must be a pair of integers [start, end]")
        
        if bounds[0] < 0 or bounds[1] > len(text):
            raise IndexError(f"Index out of range. String length is {len(text)}")

    def slice_str(substring, start: int = -1, end: int | None = None) -> str:
        """Extract substring from a given string using Pythonic slicing."""
        
        if isinstance(start, int):
            return substring[start:]
            
        elif isinstance(end, (int, float)):
            try:
                start_idx = len(substring) - end + 1
            
            except TypeError as e:
                raise ValueError(f"Invalid slice value for {substring} : {e}") from None
        
        else:
            
            return substring[start:end]
        
    def get_bounds(bounds):
        if isinstance(bounds, int):
            start = bounds

        elif isinstance(bounds, float):
            try:
                
                start_idx = round(len(substring) - bounds + 1)
                
            except TypeError as e:
                raise ValueError(f"Invalid slice value for {substring} : {e}") from None
            
        else:
            
            return substring

if __name__ == '__main__':
    pass
