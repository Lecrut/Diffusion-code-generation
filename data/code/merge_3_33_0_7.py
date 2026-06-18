import re

def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string using regular expressions,
    which is generally faster than repeated character iteration in Python due to C-level implementation.

    Args:
        text (str): The input string containing potential whitespace.

    Returns:
        str: A new string with no whitespace characters.
    """
    return re.sub(r"\s", "", text)

if __name__ == '__main__':
    # Sample test cases hard-coded to ensure the script runs without user input or external dependencies
    samples = [
        "Hello World!",          # Single spaces between words
        "\t\n\r \t Hello\tWorld!\r\n",  # Mixed tabs, newlines, carriage returns, and spaces
        "   Leading spaces and trailing ones   ",     # Whitespace at both ends
        "NoSpacesHere123...",    # String without any whitespace (should remain unchanged)
        "",                      # Empty string
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f"Input:  {repr(sample)}")
        print(f"Output: {repr(result)}")