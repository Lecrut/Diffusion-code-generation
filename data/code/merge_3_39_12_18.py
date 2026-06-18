def extract_substrings(phrase: str, indices: list[int]) -> list[str]:
    """Extract substrings from a phrase based on character indices."""
    if not isinstance(indices, list):
        raise TypeError("Indices must be provided as a list.")
    
    extracted = []
    for idx in indices:
        try:
            start_idx = int(idx)
            end_idx = None
            
            # Handle single index meaning "from this point to the end" or 
            # if it's actually a pair separated by space/string, but per task spec 
            # we assume list of integers. If an integer is negative in Python slicing logic,
            # let's strictly follow positive indexing as implied by typical user extraction tasks
            # unless specified otherwise. We will treat them as 0-based inclusive start indices only?
            # Re-reading: "list of character indices" usually implies positions to extract from.
            # To make it robust and useful, we assume each index is a starting position 
            # extracting up to the end of string for simplicity unless specified otherwise,
            # OR we could interpret as [start, length] pairs but that complicates without explicit instruction.
            
            # Given typical "extract by indices" tasks often mean: extract substring from idx to len(phrase)
            # Let's assume each integer is a start index extracting until the end of phrase for consistency.
            
            if not isinstance(idx, int):
                raise ValueError(f"Index must be an integer, got {type(idx).__name__}")

            extracted.append(phrase[start_idx:])
        except (ValueError, IndexError) as e:
            print(f"Warning: Invalid index '{idx}' at position in list. Error details suppressed for safety.") 
            # We continue processing instead of crashing to fulfill "clear error handling" without stopping execution entirely
    
    return extracted

if __name__ == '__main__':
    phrase = "Python scripting is powerful and flexible."
    indices = [3, 12, -5] 
    
    try:
        result_substrings = extract_substrings(phrase, indices)
        
        # Print results with clear formatting indicating which index produced what substring
        print("Extracted substrings based on provided character indices:")
        for idx in range(len(indices)):
            if isinstance(indices[idx], int):
                start_idx = int(indices[idx])
                end_idx = len(phrase) + 1 # Extend past length to avoid IndexError when slicing with negative or out-of-bounds logic handling below
            
                try:
                    actual_start = max(0, start_idx % len(phrase)) if isinstance(start_idx, (int, float)) else int(indices[idx]) 
                    
                    substrings_to_print = []
                    for val in indices:
                        v_int = int(val)
                        s_val = phrase[v_int:]
                        print(f"Index {val}: '{s_val}'")
                except Exception as inner_e:
                    print(f"Error processing index value: {inner_e}")

    except Exception as e:
        print("General error occurred during execution.")