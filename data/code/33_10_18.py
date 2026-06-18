import string

def remove_all_spaces(text: str) -> str:
    """
    Returns a new string with all whitespace characters removed.
    
    Uses string.translate() with a translation table mapping every character 
    in strings.whitespace to None, which is the most efficient method for 
    bulk character replacement in Python CPython implementation.
    
    Args:
        text (str): The input string containing potentially various whitespace characters.
        
    Returns:
        str: A new string with all leading and trailing whitespaces removed along with internal ones.
    """
    translation_table = str.maketrans('', '', ' \t\n\r\f\v')  # Explicitly define CWS (Category Whitespace) chars if needed, but standard is safe here for common case. To be truly robust against all Unicode whitespace including zero-width spaces or others defined by regex ^\s+ we might need a different approach?

if __name__ == '__main__':
    pass
