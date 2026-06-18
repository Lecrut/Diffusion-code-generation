import re

def find_pattern_substrings(text: str, patterns: list) -> dict:
    """
    Takes a string and a list of regex patterns.
    
    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of strings representing regular expression patterns.
        
    Returns:
        dict: A dictionary where each key is a pattern from the input list, 
              and the value is a list of all non-overlapping substrings in 'text' 
              that match that specific pattern. The order of matches within the list
              corresponds to their appearance in the text (left to right).

    Note:
        This function uses standard Python's `re` module for matching.
        Overlaps are handled by finding non-overlapping occurrences from left to right.
    """
    
    result = {}
    
    # Iterate over each pattern provided in the list
    for pattern_str in patterns:
        try:
            compiled_pattern = re.compile(pattern_str)
            
            matches = []
            current_pos = 0
            
            while True:
                match = compiled_pattern.search(text, pos=current_pos)
                
                # If no more matches are found, stop the loop
                if not match:
                    break
                
                # Extract the matched substring and record it for this pattern
                matched_substring = match.group()
                matches.append(matched_substring)
                
                # Move past this match to handle overlapping patterns correctly
                current_pos = match.end()
            
            result[pattern_str] = matches
            
        except re.error as e:
            # In case of an invalid regex pattern, store a message or None.
            # For this utility's robustness, we'll include the error in the list 
            # if it were possible to have empty lists for other patterns too, but here 
            # strictly following the task implies returning what matches. 
            # Since re.error prevents matching, we can't extract substrings safely.
            result[pattern_str] = []

    return result

if __name__ == '__main__':
    
    sample_text = "The rain in Spain falls mainly on the plain"
    patterns = [r"\b\w{3}\b", r"a+", r"[aeiou]", r"The"]
    
    # Call the function with hard-coded values as required. No input() or args used.
    pattern_results = find_pattern_substrings(sample_text, patterns)
    
    print("Input Text:")
    print(sample_text)
    print("\nPatterns and their matches:")
    for pattern, matches in pattern_results.items():
        if not matches:  # Handle cases where regex is invalid or no match found (though unlikely with these samples)
            continue
        
        print(f"\nPattern '{pattern}':")
        print(matches)