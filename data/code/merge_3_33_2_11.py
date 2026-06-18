import re

def process_string(text: str) -> str:
    """
    Removes all internal and external spaces from a given string using regex.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    # Replace all types of whitespace with an empty string
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_input = "This is   a multi\nline  string.\nHere we go!"

    result = process_string(sample_input)
    
    # Write the cleaned output to standard output as if via file I/O best practices
    print(result, end='')