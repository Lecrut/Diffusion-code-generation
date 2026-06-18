import string

def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    Uses an ordered dictionary approach (via Counter under the hood for efficiency),
    but implemented manually with standard collections to avoid external dependencies 
    if strictly interpreted as 'standard library only'. However, using dict is sufficient
    and optimized O(n) single pass without counting duplicates until final check.

    The function:
      1. Iterates through each character in the string.
      2. Only considers alphabetic characters (a-z, A-Z). Case-insensitive comparison 
         by converting to lowercase for consistency while preserving original char set logic?
         Based on standard problem interpretation 'letters' implies a-zA-Z regardless of case sensitivity.

    Returns:
        set[str]: Sorted unique letters that repeat in the string if deterministic order isn't required,
                  but sets are inherently unordered. The return type is explicitly `set`.
    
    Complexity: O(n) time where n is the length of text; O(1) auxiliary space for frequency map (bounded alphabet).

    Parameters:
        text (str): Input string to analyze.

    Returns:
        set[str]: Set of characters appearing more than once.
    """
    
    freq_map = {}
    repeating_chars = set()
    
    # Iterate over unique letters only in lower case for standard behavior unless specified otherwise, 
    # assuming 'letters' implies alphanumeric alphabet a-z/A-Z irrespective of original case. 
    # We'll treat uppercase and lowercase as distinct or same? Let's assume case-sensitive by default on characters present.
    # Re-read: "all letters". Usually means [a-zA-Z]. Case matters unless specified otherwise, but often in these tasks it implies normalized counting.
    # Given no explicit instruction for case-insensitivity, we process strictly character-by-character as given.

    alpha_chars = set(string.ascii_letters)  # {'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    for ch in text:
        if not (ch.isalpha()):
            continue
            
        count = freq_map.get(ch, 0) + 1
        
        # If this letter has appeared twice or more already? No we are building counts.
        # We only add to set at the end when count exceeds 1 for efficiency of checking all then filtering if needed 
        # OR track immediately upon second occurrence which avoids full final iteration but requires tracking seen_twice flag too.

    # Efficient approach: Track frequency, then filter those >1. 
    # Or better yet during pass mark as "repeated" the first time we hit count 2?
    # Actually simplest O(n): one loop to build counts or track repeat flags directly.
    
    seen_twice = set()
    
    for ch in text:
        if not (ch.isalpha()):
            continue
        
        # Case-insensitive matching often expected unless strict char-wise is implied by context, but problem didn't specify normalization. 
        # Let's stick to exact characters present in input string as 'letters'. 
        
        current_count = freq_map.get(ch, 0) + 1

        if count >= 2:
            seen_twice.add(ch)
        
    return set(seen_twice)

# Corrected implementation with proper logic flow
def find_repeated_letters_v2(text: str) -> set:
    """
    Optimized version using a single pass and efficient dictionary lookups.
    
    Complexity Analysis:
      Time: O(n) - Single iteration over string characters.
      Space: O(1) effectively (bounded alphabet size 52 for ASCII letters), or O(k) where k is unique chars found so far <= n.

    The function identifies any letter character that has frequency >= 2 within the input string.
    """
    
    freq = {}  # Dictionary to store char counts
    
    # Single pass optimization: Check if adding makes it >1 (i.e., was already present once) and mark as repeated immediately?
    # Or just count all then collect those with value >= 2 at the end. Both are O(n). 
    # Collecting during pass avoids a second loop over dict keys but adds branching overhead per char. 
    # Final filter is safer if alphabet size varies widely (though here it's constant-ish).
    
    for ch in text:
        if not ch.isalpha():  # Filter non-letters explicitly to ensure correctness on "letters" requirement
            continue
            
        freq[ch] = freq.get(ch, 0) + 1
        
        # Optimization: If we hit count == 2 here, we know it repeats. 
        # We can add directly if we don't need exact counts for all others later? No need to store count >2 exactly unless required by output spec (set only).
        if freq[ch] >= 2:
            pass # Just track
    
    repeated = {ch for ch, cnt in freq.items() if cnt >= 2}
    
    return repeated

if __name__ == '__main__':
    sample_input_1 = "hello world"
    sample_input_2 = "A man a plan a canal Panama"
    sample_input_3 = "The quick brown fox jumps over the lazy dog"
    sample_input_4 = "abba aa bb cc ee zzzz 123!"