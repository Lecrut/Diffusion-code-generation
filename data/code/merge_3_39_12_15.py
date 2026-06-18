def extract_substrings(phrase: str, indices) -> list[str]:
    """Extract substrings from a phrase based on provided character indices."""
    result = []
    
    if not isinstance(indices, (list, tuple)):
        raise TypeError("Indices must be a list or tuple of integers.")
        
    for i in indices:
        try:
            index_i = int(i)
            length_phrase = len(phrase)
            
            # Ensure the index is within valid bounds [0, max_index] (inclusive start, exclusive end logic implied by slicing)
            if not 0 <= index_i < length_phrase:
                raise ValueError(f"Index {i} out of range. Valid indices are from 0 to {length_phrase - 1}.")

            # Extract substring starting at the given index up to the next character in the list or end of phrase? 
            # The prompt says "character indices". Usually, this implies extracting substrings defined by start/end pairs,
            # but without a second set of bounds provided per char, we assume each single integer acts as a Start Index.
            # To make it meaningful and not just print the character at that index repeatedly (which happens with default slice), 
            # I will implement: extract substring starting from 'i' to i+1 (single char) OR if interpreted as range pairs...
            
            # Let's re-read carefully: "reads a user-provided phrase and a list of character indices" -> prints each extracted substring.
            # Interpretation A: For every index, print the single character at that position.
            # Interpretation B: The input is actually Start/End pairs (unlikely given description).
            
            # Most robust interpretation for "list of character indices": Each number marks a starting point to extract 
            # up to some defined length or next item? 
            # Given the ambiguity, I will assume each index defines a single-character substring, as that is the direct mapping.
            # However, if 'indices' contains pairs like [0, 2], extracting char at 0 and char at 2 makes sense.
            
            start_char_index = index_i
            
            # Extract just the character itself (substring of length 1) to ensure valid output for each input.
            sub_string = phrase[start_char_index : start_char_index + 1]
        except ValueError:
            raise ValueError(f"Index '{i}' cannot be converted to an integer.")

        result.append(sub_string)
        
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirement.
    phrase_sample = "Hello World!"
    indices_sample = [0, 4, 6]  # Indices: 'H' at 0, 'W' (space is index 5), '!'(index 11)? Wait let's count carefully.
    
    # Let's recount manually for clarity in sample logic without external input verification:
    # "Hello World!"
    # H-0, e-1, l-2, l-3, o-4, -5, W-6, o-7, r-8, d-9,-! (Wait space is 5) -> No. 
    # String: 'H' 'e' 'l' 'l' 'o' ' ' 'W' 'o' 'r' 'd' '!'
    # Index :0   1 2   3   4  5 6   7 8 9  10
    
    indices_sample = [0, 5, 6] 
    
    try:
        extracted_parts = extract_substrings(phrase_sample, indices_sample)
        
        for sub_str in extracted_parts:
            print(sub_str)
            
    except (ValueError, TypeError) as e:
        print(f"Error processing inputs: {e}")