import re

def extract_pattern_occurrences(input_string: str, pattern: str) -> list[str]:
    """
    Extracts all non-overlapping occurrences of a specific pattern from an input string using regular expressions.

    Args:
        input_string (str): The source text to search within.
        pattern (str): The regex pattern to match against the text.

    Returns:
        list[str]: A list containing each matched substring found in non-overlapping order.
    """
    matches = re.findall(pattern, input_string)
    return matches

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_input = "The rain is spam."
    test_pattern = r"\w+"

    result = extract_pattern_occurrences(test_input, test_pattern)
    
    print("Matches found:")
    for match in result:
        print(match)