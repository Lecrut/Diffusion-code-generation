import re

def find_pattern_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex patterns, returning a dictionary mapping 
    each pattern to a list of all non-overlapping substrings in the input text that match it.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regular expression strings.

    Returns:
        dict[str, list[str]]: A dictionary where keys are pattern strings and values 
                             are lists of matching substrings found in the text for that pattern.
    
    Note: Matches are non-overlapping. If a match is found at index i with length l, 
          subsequent searches start from index i + l.
    """
    results = {pattern: [] for pattern in patterns}

    # Compile all regex patterns to avoid repeated compilation overhead during iteration if needed later,
    # though here we iterate once per text pass which is efficient enough for typical use cases.
    
    for pattern_str in patterns:
        try:
            compiled_pattern = re.compile(pattern_str)
        except re.error as e:
            # In case of invalid regex, store an empty list or handle gracefully depending on requirements.
            # Here we assume valid input per task description but include a silent fallback to avoid crashing.
            continue

        matches_found = []
        
        start_index = 0
        
        while True:
            match = compiled_pattern.search(text, pos=start_index)
            
            if not match:
                break
            
            matched_substring = match.group()
            # Add the substring only once per pattern instance in this pass (non-overlapping logic handled by 'pos')
            matches_found.append(matched_substring)
            
            start_index = match.end()

        results[pattern_str] = matches_found

    return results

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_text = "The rain in Spain falls mainly in the plain."
    
    patterns_to_test = [
        r"\b\w{3}\b",           # Matches words of exactly 3 letters (case-sensitive)
        r"ain",                 # Matches substring 'ain'
        r"[aeiou]",             # Matches any vowel character
        r"T|t",                 # Matches uppercase or lowercase T
    ]

    matches_output = find_pattern_matches(test_text, patterns_to_test)

    print("Input Text:")
    print(test_text)
    
    print("\nPattern Matching Results:")
    for pattern, matched_substrings in matches_output.items():
        if not matched_substrings:  # Skip empty results to keep output clean unless desired otherwise.
            continue
        print(f"Pattern '{pattern}':")
        for match in matched_substrings:
            print(f"  - {match}")