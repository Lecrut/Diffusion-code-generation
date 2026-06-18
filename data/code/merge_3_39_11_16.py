import sys

class StringExtractor:
    """
    A class to efficiently extract non-overlapping substrings from a string 
    based on provided delimiter positions.
    
    Attributes:
        input_string (str): The source string to process.
        delimiters (list[int]): List of integer indices representing delimiter positions.
        
    Methods:
        get_substrings(): Returns a list of non-overlapping substrings extracted between delimiters.
    """

    def __init__(self, input_string: str, delimiters: list):
        self.input_string = input_string
        # Ensure delimiters are sorted and unique for consistent processing
        self.delimiters = sorted(list(set(delimiters)))
        
        if not 0 <= min(self.delimiters) < len(input_string):
            raise ValueError("All delimiter positions must be within the bounds of the input string.")

    def get_substrings(self) -> list:
        """
        Extracts all non-overlapping substrings from the input string based on 
        the provided delimiter positions. Substrings are defined as segments between consecutive delimiters,
        including those before the first and after the last delimiter if they exist within bounds.

        Returns:
            list[str]: A list of extracted substring strings.
        """
        substrings = []
        
        # Add segment before the first delimiter (if it exists)
        start_index = 0
        for i, delim_pos in enumerate(self.delimiters):
            if i == 0 and delim_pos > 0:
                substrings.append(self.input_string[start_index:delim_pos])
            
            end_index = delim_pos + 1
            
            # Add segment between current delimiter and next one (or end of string)
            if i < len(self.delimiters):
                next_delim = self.delimiters[i + 1]
                substrings.append(self.input_string[end_index:next_delim])
            else:
                substrings.append(self.input_string[end_index:])

        return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    source_text = "Hello, world! This is a test."
    delimiter_indices = [6, 12, 18]

    extractor = StringExtractor(source_text, delimiter_indices)
    result_substrings = extractor.get_substrings()

    print("Extracted Substrings:")
    for idx, sub in enumerate(result_substrings):
        print(f"Substring {idx + 1}: '{sub}'")