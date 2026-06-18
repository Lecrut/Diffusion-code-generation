import sys

def remove_spaces(text: str) -> str:
    """
    Removes all spaces from a given string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters.
    """
    return ''.join(char for char in text if not (' ' <= char <= '\t'))

def main():
    # Hard-coded sample values as per requirements
    # No user interaction, network access, or file I/O is performed
    samples = [
        "Hello World",
        "Python Programming",
        "Data Science"
    ]
    
    result = ""
    
    for text in samples:
        cleaned_text = remove_spaces(text)
        result += cleaned_text
    
    # Output the concatenated result without spaces between words from different lines (which were just sample strings here)
    print(result)

if __name__ == '__main__':
    main()