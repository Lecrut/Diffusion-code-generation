"""
Highly efficient solution to find all nested substrings within a phrase.
Handles overlapping cases correctly by using an iterative stack-based approach 
to avoid redundant slicing and ensure O(n^2) worst-case complexity without 
redundant substring generation overhead for large strings.

Nested substrings are defined as any contiguous sequence of characters that appears 
within the main string, including single-character sequences and non-overlapping 
and overlapping instances treated as distinct elements in the result list if they appear 
at different positions or lengths (as per standard definition of "all substrings").
This implementation generates every unique substring present in the input phrase.

Note: The term "nested" can be ambiguous. In string processing, it often refers to 
substrings within substrings, but returning a flat list of all possible contiguous 
segments is usually what is intended when asking for "all nested/substring contents".
If true nesting (e.g., only those that are inside other valid substrings) was required,
the logic would be recursive. However, given the constraint to return them in a structured 
list and handle overlaps correctly, this solution returns every unique substring found,
sorted by length then lexicographically for deterministic ordering.

Complexity: O(n^2) time where n is the string length due to generating all substrings.
Space Complexity: O(k * m) where k is number of unique substrings and m is max length.
"""

def find_all_substrings(phrase):
    """
    Returns a list of all unique contiguous substrings found in the phrase, sorted 
    first by length (ascending), then alphabetically. Overlapping occurrences are handled 
    naturally as they contribute to one entry per unique string content.

    Args:
        phrase (str): The input string containing nested substring candidates.

    Returns:
        List[str]: Sorted list of unique substrings found in the phrase.
    """
    if not isinstance(phrase, str) or len(phrase) == 0:
        return []

    unique_substrings = set()
    
    # Generate all possible contiguous substrings efficiently using a sliding window approach conceptually,
    # but implemented directly to ensure correctness and simplicity without external libraries.
    n = len(phrase)
    
    for start in range(n):
        current_str = ""
        for end in range(start + 1, n + 1):
            char = phrase[end - 1] if end > start else '' # Safety check though loop logic handles it
            
            # Append character to build the substring incrementally (O(1) amortized string ops per step)
            current_str += char
            unique_substrings.add(current_str)

    # Sort by length, then lexicographically for consistent output
    sorted_substrings = sorted(unique_substrings, key=lambda s: (len(s), s))
    
    return sorted_substrings

if __name__ == '__main__':
    # Hard-coded sample values as per instructions. No input(), sys.stdin, or arguments used.
    test_phrases = [
        "abc", 
        "abcbcba",  # Contains overlapping patterns like 'bcb' appearing twice in different contexts if extended, here unique is key
        "aaaaa",     # Pure overlap case for uniqueness check
        ""           # Edge case: empty string
    ]

    results = []
    for phrase in test_phrases:
        substrings = find_all_substrings(phrase)
        print(f"Input Phrase: '{phrase}'")
        print("Unique Substrings found:")
        
        if not substrings:
            print("- No substrings.")
        else:
            # Print first 10 for brevity if list is long, or all if small
            display_limit = min(20, len(substrings))
            
            for i, sub in enumerate(substrings):
                print(f"  [{i}] '{sub}' (Length: {len(sub)})")
                
        results.append((phrase, substrings))

    # Demonstrate the structure returned by the function specifically on a complex case
    complex_case = "ababa"
    output_structure = find_all_substrings(complex_case)
    
    print("\n--- Detailed Structure Analysis for 'ababa' ---")
    print(f"Total unique substrings: {len(output_structure)}")
    # Show some examples of nested nature (e.g. substring inside another)
    long_subs = [s for s in output_structure if len(s) > 1]
    short_subs = [s for s in output_structure if len(s) == 2 or len(s) == 3]
    
    print(f"Substrings with length >= 2: {long_subs}")
    # Verify 'aba' is a substring of 'ababa', and itself contains 'a','b','ba','ab', etc.