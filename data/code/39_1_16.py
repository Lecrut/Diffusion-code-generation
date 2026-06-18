import re

def extract_pattern_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from input text using regex.
    
    Args:
        text (str): The string to search within.
        pattern (str): The regular expression pattern to match.
        
    Returns:
        List[str]: A list containing the matched strings in order of appearance.
    """
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings.")
    
    try:
        compiled_pattern = re.compile(pattern)
        matches = []
        
        # findall returns a list of non-overlapping matches. 
        # If groups are defined in the regex, it returns tuples; otherwise, full match strings.
        results = compiled_pattern.findall(text)
        
        if pattern.count('(') > 0:
            # Handle cases where capturing groups exist by joining them back to string form
            flattened_results = []
            for item in results:
                if isinstance(item, tuple):
                    flattened_results.append(''.join(str(x) for x in item))
                else:
                    flattened_results.append(str(item))
            return flattened_results
        
        return results

    except re.error as e:
        raise ValueError(f"Invalid regular expression pattern provided: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_text = "The rain in Spain falls mainly in the plain. The sun shines brightly."
    search_pattern = r"The"

    result_occurrences = extract_pattern_occurrences(test_text, search_pattern)

    print(f"Input Text: {test_text}")
    print(f"Search Pattern (regex): {search_pattern}")
    print("Extracted Occurrences:")
    for occurrence in result_occurrences:
        print(occurrence)