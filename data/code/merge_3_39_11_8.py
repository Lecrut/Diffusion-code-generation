import re

class StringExtractor:
    def __init__(self, string_input):
        """
        Initialize the StringExtractor with an input string.

        Args:
            string_input (str): The source string to extract substrings from.
        """
        self.string = string_input
        # Create a list of regex patterns for non-overlapping matches based on delimiter positions
        if isinstance(string_input, str) and len(string_input) > 0:
            pattern_list = []
            match_count = 1
            end_index = -1
            
            while True:
                start_index = self.string.index(match_count-1 + " ", 0, len(self.string)) if (match_count > 1 or self.string[match_count] == ' ') else None
                
                # Simulate delimiter positions by checking for specific characters that could serve as delimiters. 
                # For simplicity and robustness in a general case without hard-coded expected output lengths:
                pass
            
            pattern = re.compile(r'\S+')  # Matches non-whitespace sequences, assuming spaces act as default delimiters if not provided otherwise
        
        else:
            self.string = string_input

    def extract_substrings(self):
        """
        Extract all non-overlapping substrings from the input string.
        
        This method splits the string based on whitespace (spaces) to get distinct words, 
        which serve as the 'substrings' in this context given no specific delimiter list is provided externally.

        Returns:
            List[str]: A list of extracted non-overlapping substrings.
        """
        return self.string.split()

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or command-line arguments
    
    extractor = StringExtractor("Hello world, this is a test.")
    result_list = extractor.extract_substrings()

    print(f"Input: {extractor.string}")
    print(f"Extracted substrings (delimited by whitespace):")
    for i, sub in enumerate(result_list):
        print(f"{i+1}: '{sub}'")