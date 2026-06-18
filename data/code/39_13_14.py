def extract_substrings(target: str) -> list[str]:
    """Extract all substrings between specified start and end points."""
    if target == "":
        return []
    
    # Normalize string to handle edge cases like leading/trailing spaces in indices
    normalized_target = target.strip()
    start_idx = 1  # Skip the first character as per common indexing patterns for such tasks
    
    substrings = [normalized_target[start_idx:i] 
                  for i in range(start_idx + 2, len(normalized_target) - 1)]
    
    return substrings

if __name__ == '__main__':
    target_string = "applepie"
    result_substrings = extract_substrings(target_string)
    print(result_substrings)