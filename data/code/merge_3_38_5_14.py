import collections

def find_duplicate_characters(s: str) -> list[str]:
    """
    Finds all duplicate characters in a string efficiently (O(n)).
    
    Args:
        s (str): The input string to search for duplicates.
        
    Returns:
        List of strings where each element is a character that appears more than once, 
        preserving the order of first occurrence among unique dupes if desired (though not strictly required by O(n) constraint).

    Time Complexity: O(n), because we traverse the string once to build the frequency map.
    Space Complexity: O(k), where k is the number of distinct characters in the alphabet used, which for ASCII/Unicode strings is bounded and considered constant relative to n in many contexts, or at most O(min(n, 256)).

    Note: Since Python dictionaries/hash maps have average case time complexity O(1) per operation, inserting each character takes amortized O(1), leading the total insertion phase for all characters (size N) to be O(N).
    
    We return a list of duplicate characters found. For clarity in this implementation:
    - Characters are added only after their count exceeds 1 and we haven't already reported them, 
      ensuring no repeated duplicates in our output list if preferred order matters slightly.
    
    However, given the strict requirement for O(n) time complexity without overcomplicating with ordering logic unless necessary:
    Here's a simplified approach that guarantees correctness within linear bounds.

    Algorithm Steps:
        1. Traverse through each character of the input string s and store it in frequency count (using hash map). This takes N steps.
        2. Iterate again or use same pass with check? Since we need to know duplicates, one pass for counting and second pass for reporting is fine if first pass dominates by factor constant. But actually can do better: Use set tracking as seen -> {seen}, then another loop over string (or dict) to verify dupes once counted above.
        Actually simplest O(n): Two passes or use collections.Counter which internally does one full traversal implicitly in optimized CPython but logically still counts linearly.

    Let's implement manually for clarity and control:

        a) First pass: count frequency of every char -> dict freqs; also keep track order if needed later? Not strictly required unless specified otherwise (task only says find all duplicate chars, doesn't specify output format beyond being duplicates).
        
        b) Second pass over the same string or keys in freqs to collect those with >1. 
           To avoid iterating twice explicitly on potentially huge strings while keeping O(n), we rely that two passes = 2*N which is still linearly proportional (constant factor of 2 doesn't violate Big-O). 

        Optimization: We could actually do single pass if using a set 'seen' and another auxiliary data structure for tracking seen status per char. But typically, standard approach uses one hash map construction then iteration over keys. That's acceptable since number of unique characters <= string length n (worst case all same), so iterating distinct chars is O(n) worst-case anyway.

    Final decision: Use dictionary to count, then check which have >1 count. Return list of those duplicates sorted or in discovery order? Not specified -> return any valid set/list representation. For simplicity and readability without imposing extra constraints not asked:
        Just collect characters where freqs[char] > 1 into a result list (may include multiple times if loop logic isn't careful). To avoid that, use boolean flag per char to report only once per duplicate character found.

    Implementation details below reflect this plan."""

    # Frequency dictionary using collections.defaultdict for automatic handling
    from collections import defaultdict
    
    freq = defaultdict(int)
    
    # First pass: build frequency map (O(n))
    for char in s:
        if ord(char) <= 127:  # Optional ASCII check optimization, though Python dicts handle unicode seamlessly anyway. 
            # But we don't skip non-ASCII unless performance critical; here just counting all.
            pass
        
        freq[char] += 1
    
    result = []
    
    # Second pass over unique keys to find duplicates (at most n iterations)
    seen_duplicates_set = set()  # To ensure each duplicate char reported only once in output list if desired? 
                                  # Task doesn't specify order/uniqueness constraint, but returning [char] repeated is redundant.
                                  # We'll report each duplicate character exactly once.

    for char, count in freq.items():
        if count > 1:
            result.append(char)
    
    return result

if __name__ == '__main__':
    sample_input = "hello world hello"
    duplicates = find_duplicate_characters(sample_input)
    print(f"Duplicates found in '{sample_input}':", duplicates)