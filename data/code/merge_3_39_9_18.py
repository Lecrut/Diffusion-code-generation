"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.
Returns results in a structured list of dictionaries containing start index, end index, 
and substring content.
"""

def find_nested_substrings(phrase: str) -> list[dict]:
    """
    Finds all possible contiguous substrings (nested levels implied by any non-empty slice).
    
    This function generates every unique substring from the input phrase.
    It handles overlapping cases naturally because it iterates through all start and end indices,
    capturing overlaps in its output structure rather than filtering them out.
    
    Args:
        phrase (str): The input string to analyze.
        
    Returns:
        list[dict]: A list of dictionaries with keys 'start', 'end', and 'substring'.
                    Indices are 0-based, inclusive start, exclusive end.
    """
    results = []
    
    # Iterate through all possible starting positions
    for i in range(len(phrase)):
        current_char = phrase[i]
        
        # Optimization: If the character is whitespace or empty string handling isn't needed 
        # as we iterate by index, but let's ensure valid slicing.
        if not isinstance(current_char, str):
            continue
            
        # Iterate through all possible ending positions for this start
        for j in range(i + 1, len(phrase) + 1):
            substring = phrase[i:j]
            
            # Only add non-empty substrings to the results list
            if substring:
                results.append({
                    "start": i,
                    "end": j,
                    "substring": substring
                })
                
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access used.
    
    sample_phrase = "abcde"
    
    print(f"Analyzing phrase: '{sample_phrase}'")
    substrings_found = find_nested_substrings(sample_phrase)
    
    print("\nAll nested substrings found:")
    for item in substrings_found:
        s_info = f"[{item['start']}:{item['end']}]"
        print(f"  {s_info} -> '{item['substring']}'")
        
    # Verification with a more complex overlapping case if needed, 
    # though the logic above handles overlaps by definition of slicing.
    
    sample_phrase_complex = "ababa"
    print("\n--- Complex Overlapping Case: 'ababa' ---")
    substrings_found_complex = find_nested_substrings(sample_phrase_complex)
    
    for item in substrings_found_complex:
        s_info = f"[{item['start']}:{item['end']}]"
        # Print only unique substring content to demonstrate distinct values, 
        # but the list itself contains all instances including overlaps.
        print(f"  {s_info} -> '{item['substring']}'")
        
    total_count = len(substrings_found_complex)
    print(f"\nTotal substrings identified: {total_count}")