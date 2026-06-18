import bisect

class StringExtractor:
    def __init__(self):
        """Initialize the StringExtractor class."""
        pass
    
    def extract_substrings(self, input_string, delimiter_positions):
        """
        Extract all non-overlapping substrings from a given input string 
        based on provided delimiter positions.
        
        Args:
            input_string (str): The source string to process.
            delimiter_positions (list of int): A list of indices where delimiters occur.
            
        Returns:
            list[str]: A list of extracted substrings between consecutive delimiters or 
                      the start/end of the string.
        
        Note: Delimiter positions are assumed to be sorted and within valid bounds [0, len(input_string)-1].
              Adjacent or identical positions result in empty strings being skipped if desired, 
              but here we extract exactly what is between them as per standard interval logic.
        """
        if not input_string or not delimiter_positions:
            return []

        # Ensure delimiter positions are sorted and valid (0 <= pos < len(input_string))
        filtered_positions = [pos for pos in set(delimiter_positions) 
                             if 0 <= pos < len(input_string)]
        
        is_sorted_and_unique = True

if __name__ == '__main__':
    pass
