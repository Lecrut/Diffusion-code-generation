"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.
Returns results in a structured list format: [{'start': int, 'end': int, 'substring': str}]
Sorted by start index (ascending), then by length (descending).
"""

def find_nested_substrings(phrase):
    """
    Finds all non-empty substrings within the given phrase.
    
    A substring is defined as any contiguous sequence of characters from the original string.
    This includes overlapping occurrences and single-character strings.
    
    Args:
        phrase (str): The input string to analyze.
        
    Returns:
        List[Dict]: A list of dictionaries, each containing 'start', 'end', and 'substring'.
                   Sorted by start index ascending, then by length descending.
    """
    if not isinstance(phrase, str) or len(phrase) == 0:
        return []

    results = []
    
    # Iterate over all possible starting positions
    for i in range(len(phrase)):
        current_char = phrase[i]
        
        # Optimization: If the character is empty (handled by loop), continue. 
        # We start a substring at index i with length 1, then extend it.
        
        for j in range(i + 1, len(phrase) + 1):
            substr_start = phrase[i:j]
            
            results.append({
                'start': i,
                'end': j - 1, # End index is inclusive (j-1), length is j-i
                'substring': substr_start
            })

    # Sort the results: 
    # Primary key: start index (ascending)
    # Secondary key: substring length (descending) to prioritize longer matches at same position
    results.sort(key=lambda x: (x['start'], -len(x['substring'])))
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access used.
    phrase = "ABCAB"

    nested_substrings = find_nested_substrings(phrase)

    print(f"Input Phrase: '{phrase}'")
    print("-" * 40)
    
    for item in nested_substrings:
        start_idx = item['start']
        end_idx = item['end']
        substr_str = item['substring']
        
        # Format output clearly showing indices and content
        marker = f"[{start_idx}:{end_idx}]" if len(substr_str) > 0 else "[empty]"
        print(f"Start: {start_idx}, End: {end_idx}, Length: {len(substr_str)}, Substring: '{substr_str}'")

    # Verification of count logic (optional debug info for robustness check in local run context)
    total_count = len(nested_substrings)
    expected_total = (phrase.count('') + 1) * phrase.length if hasattr(phrase, 'length') else None 
    # Since Python strings don't have a length property method like JS/Java often used for O(N^2), 
    # we rely on the algorithmic generation which is mathematically N*(N+1)/2 substrings.
    
    print("-" * 40)
    print(f"Total nested substrings found: {total_count}")