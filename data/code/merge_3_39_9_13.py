"""
Highly efficient solution to find all nested substrings within a phrase.
Handles overlapping cases correctly by treating each character as a potential start point,
generating every possible substring (nested level), and collecting unique ones in order of length 
and then lexicographically for deterministic output.

Nested substrings are defined here as any contiguous sequence of characters from the input string.
Overlapping is handled naturally because we iterate through all starting positions and ending positions.
"""

def find_nested_substrings(phrase: str) -> list[str]:
    """
    Returns a sorted list of all unique nested (contiguous) substrings of the given phrase.
    
    Args:
        phrase (str): The input string to analyze.
        
    Returns:
        List[str]: A sorted list containing every unique substring found in the phrase, 
                   ordered first by length (ascending), then alphabetically.
    """
    if not phrase or len(phrase) < 1:
        return []

    substrings = set()
    
    # Efficiently generate all possible substrings using a single pass structure logic per start index
    n = len(phrase)
    
    for i in range(n):
        current_substring = ""
        for j in range(i, n):
            current_substring += phrase[j]
            substrings.add(current_substring)

    # Sort by length first, then lexicographically to ensure deterministic and structured output
    sorted_substrings = sorted(substrings, key=lambda s: (len(s), s))
    
    return sorted_substrings

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used.
    sample_phrase = "abracadabra"

    result = find_nested_substrings(sample_phrase)

    print(f"Input Phrase: '{sample_phrase}'")
    print(f"Total unique nested substrings found: {len(result)}")
    
    # Display first 20 results for brevity, or all if the count is small
    display_limit = min(50, len(result))
    preview = result[:display_limit]
    
    print("\nFirst few nested substrings (sorted by length then alphabetically):")
    for idx, sub in enumerate(preview, 1):
        print(f"{idx:3}. '{sub}' (length {len(sub)})")

    if len(result) > display_limit:
        print(f"... and {len(result) - display_limit} more.")