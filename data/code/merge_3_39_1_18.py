import re

def extract_pattern(pattern: str, text: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a pattern from input text using regex.
    
    Args:
        pattern (str): The regular expression pattern to search for.
        text (str): The string in which to search for the pattern.
        
    Returns:
        list[str]: A list containing all matched substrings found in the text.
    """
    matches = re.findall(pattern, text)
    return matches

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    search_pattern = r'\b\d{3}\.\d{2}'  # Matches IP-like addresses: e.g., "123.45"
    test_string = "Contact us at 101.99 for support, and also reach 202.88 via email."

    result = extract_pattern(search_pattern, test_string)

    print("Pattern:", search_pattern)
    print("Input text:", test_string)
    print("Matches found:")
    if not result:
        print("None")
    else:
        for match in result:
            print(match)