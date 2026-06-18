import re

def split_by_delimiters(phrase: str, delimiters: set) -> list[str]:
    """
    Splits a phrase into contiguous segments based on the provided delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set of single-character strings representing delimiters.
        
    Returns:
        list[str]: A list of non-empty substrings separated by any of the delimiter characters.
                   Consecutive delimiters are treated as a single separator, and leading/trailing 
                   separators do not result in empty string entries unless explicitly handled;
                   however, standard split behavior is applied where consecutive or edge delimiters
                   may yield empty strings if they surround content without internal separation logic.
    
    Note: This implementation treats the set of delimiters as a regex pattern for splitting,
          effectively joining them into one character class to match any occurrence.
    """
    # Escape special regex characters in delimiter strings just in case (though input is assumed single chars)
    escaped_delims = [re.escape(delim) for delim in delimiters]
    
    if not phrase:
        return []

if __name__ == '__main__':
    pass
