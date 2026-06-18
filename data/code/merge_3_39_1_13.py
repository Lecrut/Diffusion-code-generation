import re

def extract_pattern(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from text using regex.

    Args:
        text (str): The input string to search within.
        pattern (str): The regular expression pattern to match.

    Returns:
        list[str]: A list of matched strings in the order they appear in the text.
    """
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both 'text' and 'pattern' must be strings.")
    
    try:
        return re.findall(pattern, text)
    except re.error as e:
        raise ValueError(f"Invalid regular expression pattern provided: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    sample_text = "The rain in Spain falls mainly on the plain."
    
    # Define a few test patterns for demonstration purposes.
    pattern_digits = r"\d+"
    pattern_vowels_at_end = r"aeiou$"
    
    results_digits = extract_pattern(sample_text, pattern_digits)
    vowels_matched = [m.group() if hasattr(m, 'group') else m for m in re.finditer(pattern_vowels_at_end, sample_text)]

    print(f"Sample text: {sample_text}")
    print(f"Pattern to find digits ({pattern_digits}):")
    if results_digits is None or len(results_digits) == 0:
        print("No matches found.")
    else:
        for item in results_digits:
            print(item)