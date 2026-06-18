"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.
Returns results in a structured list format: each substring is represented as a dictionary 
containing 'start', 'end' (exclusive), and 'value'.
"""

def find_nested_substrings(phrase):
    """
    Finds all possible contiguous substrings of the given phrase.
    
    This function generates every unique substring by iterating through all start positions,
    then extending from each position to create end positions. It handles overlaps naturally 
    as it is a standard generation process for all sub-sequences (contiguous).
    
    Args:
        phrase (str): The input string to analyze.
        
    Returns:
        List[Dict]: A list of dictionaries, where each dictionary represents a substring with keys 'start', 'end', and 'value'.
    """
    results = []
    n = len(phrase)
    
    # Iterate over all possible start indices
    for i in range(n):
        current_start = phrase[i]
        
        # Extend the substring from index i to every subsequent index j > i
        for j in range(i + 1, n + 1):
            end_index = j - 1
            
            substrings_list.append({
                'start': i, 
                'end': end_index, 
                'value': phrase[i : end_index+1]
            })

    return substrings_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_phrase = "abc"
    
    print(f"Analyzing phrase: '{test_phrase}'")
    nested_substrings = find_nested_substrings(test_phrase)
    
    print("Found nested substrings:")
    for item in nested_substrings:
        print(item)