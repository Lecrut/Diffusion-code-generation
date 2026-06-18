import re

def extract_pattern(input_string: str, pattern_str: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from an input string using regular expressions.

    Args:
        input_string (str): The text to search within.
        pattern_str (str): The regex pattern to match against the input string.

    Returns:
        list[str]: A list containing all matched substrings in order of appearance.
    """
    if not isinstance(input_string, str) or not isinstance(pattern_str, str):
        raise TypeError("Both input_string and pattern must be strings.")

    try:
        compiled_pattern = re.compile(pattern_str)
        matches = []
        
        # Use finditer to get all non-overlapping matches efficiently
        for match in compiled_pattern.finditer(input_string):
            matches.append(match.group())
            
        return matches
    except re.error as e:
        raise ValueError(f"Invalid regular expression pattern provided: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_input = "The rain in Spain falls mainly in the plain. The sun shines bright."
    search_pattern = r"The"

    result_matches = extract_pattern(test_input, search_pattern)

    print(f"\nInput String:\n{test_input}\n")
    print(f"Search Pattern: {search_pattern}")
    print(f"Found Matches ({len(result_matches)} occurrences):\n{result_matches}")