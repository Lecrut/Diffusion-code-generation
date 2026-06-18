import sys

def remove_spaces(text: str) -> str:
    """
    Removes all internal and surrounding spaces from a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    return "".join(text.split())

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # This block runs without user input, command-line arguments, 
    # network access, or pre-existing files.
    
    samples = [
        "Hello World",
        "   Leading and trailing spaces  ",
        "Multiple   internal      spaces here.",
        "NoSpacesAtAll",
        "\t\tTabsand\nNewlines"
    ]
    
    for sample in samples:
        result = remove_spaces(sample)
        print(result, end="")