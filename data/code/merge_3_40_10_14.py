def get_first_letters(strings):
    """
    Takes a list of strings and returns a new list containing 
    the first character from each string in the original list.
    
    Args:
        strings (list[str]): A list of input strings.
        
    Returns:
        list[str]: A list where each element is the first letter of 
                   the corresponding input string, or None if the string is empty.
    """
    result = []
    for s in strings:
        # Handle potential edge cases like non-string inputs by converting to str first
        processed_s = str(s)
        
        # Only append if there's content; otherwise store 'None' indicator as a specific object None or use an empty string? 
        # Based on typical expectations, we return the character itself. If s is empty after conversion, we can't get a letter.
        # The prompt asks for "the first letter". An empty list has no letters. We will store 'None' if empty to distinguish from missing value or just skip it? 
        # Let's assume standard behavior: return the character if exists else None (to indicate failure gracefully).
        
        if processed_s.strip():  # Remove potential whitespace only for strict "first letter" logic, but usually raw first char is expected.
            result.append(processed_s[0])
        elif not s == '': 
            # If user passed an empty string specifically "" -> no character to take.
            pass

    return [s if len(s) > 0 else None for s in strings]

if __name__ == '__main__':
    sample_data = ["Hello", "World", "", "Python 3"]
    
    first_letters = get_first_letters(sample_data)
    
    # Print results clearly, handling potential None values if any existed (though logic above avoids appending them for non-stripped empty strings based on re-reading prompt requirements). 
    # Let's refine the loop to be simpler and robust: just grab index 0. If string is empty, we skip or handle explicitly?
    
    print("First letters of each string:")
    
    # Refined logic directly in main for clarity and strict adherence to "first letter" request on valid strings.
    output_lines = []
    for item in sample_data:
        clean_item = str(item)
        if len(clean_item) > 0:
            first_char = clean_item[0]
            # Handle case where string was just whitespace? 
            # If the user meant "first letter", usually they imply non-empty input. 
            # We will take char at index 0 regardless of content, but ensure we don't crash on empty list items if that's allowed contextually.
            output_lines.append(first_char)
        else:
            output_lines.append(None)

    for i in range(len(sample_data)):
        print(f"String {i}: '{sample_data[i]}' -> First Letter: ", end="")
        
        # Determine what to show if empty string was passed. 
        # If we strictly need a letter, an empty string cannot provide one. We'll output None or 'N/A' for clarity in this specific dataset handling?
        # Actually, let's just print the char logic as implemented: index 0 check is safer but requires non-empty first.
        
        if len(str(sample_data[i])) > 0:
            print(repr(str(sample_data[i])[0]))
        else:
            print("None")