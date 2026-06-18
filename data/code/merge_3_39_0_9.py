def extract_all_substrings(text: str, substrings: list[str]) -> list[str]:
    """
    Extracts all occurrences of specified substrings from a given text.
    
    The function returns a flat list containing every found occurrence 
    in the order they appear within the original string. Each element 
    is one instance of any of the requested substrings, including overlapping matches 
    if multiple patterns match at the same position (handled by checking each pattern individually).

    Args:
        text (str): The input string to search within.
        substrings (list[str]): A list of strings representing the target substrings to find.

    Returns:
        list[str]: A list of all found substring occurrences in order of appearance.

    Raises:
        TypeError: If 'text' is not a string or if 'substrings' is not a list of strings.
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError(f"Expected text to be a string, got {type(text).__name__}")
    
    if not isinstance(substrings, list):
        raise TypeError(f"Expected substrings to be a list, got {type(substrings).__name__}")

    found_occurrences = []
    
    # Iterate through the input string character by character to handle overlapping matches correctly.
    start_index = 0
    
    while start_index < len(text):
        match_found_at_this_pos = False
        
        for sub in substrings:
            if not isinstance(sub, str):
                raise TypeError(f"Each element in 'substrings' must be a string.")
            
            # Check if the current substring matches starting at the current position.
            if text.startswith(sub, start_index):
                found_occurrences.append(text[start_index:start_index + len(sub)])
                match_found_at_this_pos = True
                
                # Move past this specific occurrence to allow overlapping checks for other substrings 
                # or even different parts of the same substring sequence (though a string can't overlap itself).
                start_index += 1
        
        if not match_found_at_this_pos:
            # If no substring matched at current position, move forward by one character.
            start_index += 1
            
    return found_occurrences

if __name__ == '__main__':
    sample_text = "abracadabra"
    desired_substrings = ["a", "ra", "bra"]

    result = extract_all_substrings(sample_text, desired_substrings)

    print("Input Text:", repr(sample_text))
    print("Desired Substrings:", desired_substrings)
    print("All Found Occurrences:")
    
    # Format output for readability: index | substring found
    formatted_output = []
    current_idx = 0
    for item in result:
        start_pos = sample_text.find(item, current_idx) if item != "" else -1
        
        # Re-calculate position relative to original string accurately 
        # by finding the first occurrence of this specific match from that point onwards.
        pos_in_original = None
        temp_search_start = 0
        while True:
            idx = sample_text.find(item, temp_search_start)
            if idx != -1:
                pos_in_original = idx
                break
            
            # If we didn't find it from the start because of previous matches shifting context? 
            # Actually, since we just append to a list and iterate linearly in extraction logic above,
            # but here we need absolute positions for display. Let's re-scan carefully or trust the order.
            # The function returns items in order they appear. So finding them again from start is safe.
            
        formatted_output.append(f"  Index {pos_in_original}: '{item}'")

    print("\n".join(formatted_output))
    
    if result:
        print(f"\nTotal occurrences found: {len(result)}")