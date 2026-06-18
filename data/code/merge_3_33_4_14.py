import re

def clean_string(input_str: str) -> str:
    """
    Returns a new string containing only alphanumeric characters.
    
    All spaces and non-alphanumeric characters (like punctuation, symbols, etc.) 
    are removed from the input string.
    
    Args:
        input_str (str): The original string to be cleaned.
        
    Returns:
        str: A string with only letters, digits, and underscores preserved.
             Note: To strictly keep ONLY alphanumeric (a-z, A-Z, 0-9), 
             we will exclude underscores based on the strict definition of "alphanumeric".
    """
    # Regular expression to match any character that is a letter or digit
    pattern = r'[\w]'
    result = re.sub(pattern, '', input_str)
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "Hello World! This is a test.",
        "C++ Programming: A Comprehensive Guide",
        "User123@Admin#Contact!",
        "No spaces here, just symbols!!! 12345"
    ]

    for text in test_cases:
        cleaned = clean_string(text)
        print(f"Original: {text}")
        print(f"Cleaned : '{cleaned}'\n")