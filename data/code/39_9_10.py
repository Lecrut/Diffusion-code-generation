"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.
Returns results in a structured list format: each substring is represented as {'start': int, 'end': int, 'text': str}.
The search includes the entire string and all possible contiguous sub-sequences (nested levels).

This implementation uses an efficient O(n^2) approach to generate all substrings.
While generating every substring inherently handles overlaps by definition of contiguity,
the algorithm is optimized for memory usage compared to recursive backtracking methods 
that might duplicate work or struggle with large inputs due to stack depth limits.

Nested levels are implied: a string S contains level 0 (itself), and all its substrings represent
lower nesting depths relative to the full phrase context. The output captures every unique 
substring instance found within the input phrase boundaries, ordered by length then start position.
"""

def find_all_nested_substrings(phrase):
    """
    Finds all nested substrings within a given phrase.

    Args:
        phrase (str): The input string to analyze for nested substrings.

    Returns:
        List[Dict]: A list of dictionaries, each containing 'start', 'end', and 'text' keys.
                    Each dictionary represents one substring found in the phrase.
    
    Complexity Analysis:
        Time: O(n^2) where n is the length of the phrase (due to generating all substrings).
        Space: O(k * m) where k is the number of unique substrings and m is average substring length,
               for storing results in memory. This is optimal since we must return every instance.

    Example Usage:
        >>> find_all_nested_substrings("abc")
        [{'start': 0, 'end': 1, 'text': 'a'}, {'start': 0, 'end': 2, 'text': 'ab'}, 
         {'start': 0, 'end': 3, 'text': 'abc'}, {'start': 1, 'end': 2, 'text': 'b'}, 
         {'start': 1, 'end': 3, 'text': 'bc'}, {'start': 2, 'end': 3, 'text': 'c'}]
    """
    
    # Handle empty input gracefully
    if not phrase:
        return []

    results = []
    n = len(phrase)

    # Iterate through all possible start positions
    for i in range(n):
        current_char = phrase[i]
        
        # For each starting position, iterate through all ending positions (including itself)
        for j in range(i + 1, n + 1):
            substring_text = phrase[i:j]
            
            # Append the result with start index i and end index j (exclusive of j in slicing but inclusive conceptually here)
            results.append({
                'start': i, 
                'end': j, 
                'text': substring_text
            })

    return results

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    test_phrases = [
        "abc",                          # Simple case with 6 substrings including itself
        "",                            # Empty string edge case
        "aaaaa",                        # Overlapping identical characters (5*4/2 + 1? No, n*(n+1)/2 total) -> actually 10 unique indices pairs but text repeats. 
                                       # Wait: a(0), aa(0-2), aaa... no wait slicing is i:j
                                       # "aaaaa" length 5. Pairs (i,j):
                                       # i=0: j=1(a), j=2(aa), j=3(aaa), j=4(aaaa), j=5(aaaaa) -> 5 items
                                       # i=1: j=2(a), ... j=6? no max is n+1. 
                                       # Total substrings = n*(n+1)/2 = 5*6/2 = 15. Correct logic applies even with repeats in text content if we track indices.
        "ababa",                        # Overlapping patterns like 'a', 'b' appearing multiple times at different offsets
    ]

    print("Nested Substring Finder Results:")
    for phrase in test_phrases:
        substrings = find_all_nested_substrings(phrase)
        
        if not substrings:
            print(f"Input '{repr(phrase)}': No nested substrings found.")
        else:
            # Sorting by length descending, then start index ascending for better readability of 'nested' structure
            sorted_results = sorted(substrings, key=lambda x: (-len(x['text']), x['start']))
            
            print(f"\nInput Phrase: '{phrase}'")
            print("All Nested Substrings (sorted by length desc):")
            formatted_output = []
            for item in sorted_results:
                # Determine nesting level visually based on text inclusion if possible, 
                # but here we just list them as requested.
                formatted_output.append(f"  Start:{item['start']:2d} End:{item['end']:2d}: '{item['text']}'")
            
            print("\n".join(formatted_output))

    # Verification of specific overlapping case logic manually for "ababa":
    # Expected to capture 'a' at index 0, 2; 'b' at index 1, 3.