import re

def extract_pattern_occurrences(input_string: str, pattern: str) -> list[str]:
    """
    Extracts all non-overlapping occurrences of a specific pattern from an input string using regex.
    
    Args:
        input_string (str): The text to search within.
        pattern (str): The regular expression pattern to match.
        
    Returns:
        List[str]: A list containing the starting index and ending slice for each non-overlapping 
                   occurrence of the pattern in the input string. Each element is a tuple-like string 
                   formatted as "start:end". If no matches are found, returns an empty list.
    
    Raises:
        re.error: If the provided regular expression pattern is invalid.
    """

if __name__ == '__main__':
    pass
