import sys

def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs within the input string.
    
    If the length of the string is odd, the last unpaired character remains in place.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped adjacent pairs.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Handle empty strings explicitly for clarity
    if len(s) == 0:
        return s
    
    result = []
    
    # Iterate over the string in steps of two using slicing with stride 2
    start_index = 1
    step_size = 2
    
    while True:
        chunk_start, chunk_end = int(start_index), int(start_index + step_size)
        
        if len(s) == 0 or (chunk_end > max(1, len(s))): # Check bounds carefully including edge case of empty string handled above
            break
            
        # If the calculated end index exceeds actual length, just take what's available and stop. 
        # However, for strict pair swapping logic: we only swap if both characters exist.
        
        current_pair = s[chunk_start:chunk_end]
        
        # Swap positions within the chunk (which is always 2 chars unless truncated at end)
        swapped_pair = list(reversed(current_pair))
        
        result.extend(swapped_pair)
        
        start_index += step_size
        
        # Ensure we don't process more than available characters without creating pairs, 
        # but since we increment by 2 and check bounds above (implicitly via slice), it handles odd lengths naturally.

    return "".join(result)

if __name__ == '__main__':
    sample_string = "ab12cd34"
    
    output_result = swap_adjacent_pairs(sample_string)
    print(output_result)