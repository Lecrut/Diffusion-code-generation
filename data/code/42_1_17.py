def build_string_from_parts(parts):
    """
    Joins a list of string parts into a single string separated by spaces.
    
    This function is optimized to achieve O(n) time complexity, where n is 
    the total number of characters in all input strings combined. It avoids 
    creating intermediate lists that would require multiple passes over the data.

    Args:
        parts (list[str]): A list of string elements to be joined.
        
    Returns:
        str: The concatenated string with spaces between original substrings.
    """
    if not parts:
        return ""
    
    # Calculate total length needed for pre-allocation optimization
    total_length = sum(len(part) + 1 for part in parts[:-1]) + len(parts[-1])
    
    result_list = [''] * (total_length - 1)
    current_index = 0
    
    # Fill the list with characters from each string, skipping one position per join
    for i, part in enumerate(parts):
        if not part:
            continue
            
        start_idx = sum(len(p) + 1 for p in parts[:i]) - len(part)
        
        for j, char in enumerate(part):
            result_list[start_idx] = char
            start_idx += 1
        
        # Add space after this string if it's not the last one
        if i < len(parts) - 1:
            current_index += 1
    
    return ''.join(result_list)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "Is", "A"]
    output_string = build_string_from_parts(sample_parts)
    print(output_string)