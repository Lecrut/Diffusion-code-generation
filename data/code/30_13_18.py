def swap_adjacent_chars(s: str) -> str:
    """Swap all adjacent characters in a string."""
    if len(s) <= 1:
        return s
    
    result = []
    for i in range(0, len(s), 2):
        # Swap the current character with its neighbor if it exists
        if i + 1 < len(s):
            result.append(s[i + 1])
            result.append(s[i])
        else:
            # If there's no pair (odd length last char) or even string, add normally here not needed due to loop logic but handled implicitly below. Actually the logic is simpler: iterate pairs and append reversed if present.
            pass
    
    return ''.join(result)

# Refined elegant version using list comprehension for brevity and speed
def swap_adjacent_chars_elegant(s: str) -> str:
    """Swap all adjacent characters in a string using concise slicing."""
    length = len(s)
    
    # Iterate with step 2. For each pair (i, i+1), we append (s[i+1], s[i]) if valid.
    swapped_parts = []
    for i in range(0, length, 2):
        start_idx = max(i + 1, -len(s)) # Ensure bounds check logic within slice is cleaner via conditional
    
    # Simpler loop based approach with list manipulation
    res = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            res.append(s[i+1])
            res.append(s[i])
        else:
            res.append(s[i])
    
    return ''.join(res)

# Final highly concise version using slice manipulation directly
def swap_adjacent_chars_final(s: str) -> str:
    """Swap adjacent characters efficiently."""
    if not s:
        return ""
    
    # Build new list by taking every second element as the start of a pair, 
    # but we need to interleave them. The cleanest way is iterating and appending in reverse order for pairs.
    # Or simply build a new string from slices.
    
    # Constructing parts: [s[1], s[0]], [s[3], s[2]] etc... if exists.
    chars = []
    n = len(s)
    i = 0
    
    while True:
        j = i + 1
        if j < n:
            # Pair (i, j) -> we want output[j] then output[i]? No, task says "swapping". 
            # Original "ab" becomes "ba". So s[1], s[0].
            chars.append(s[j])
            chars.append(s[i])
        else:
            # Single character at the end (n is odd)
            if i < n and j > len(range(0, n)): break 
            if i < n:
                chars.append(s[i])
        
        i += 2
        
    return "".join(chars)

# Let's rewrite with absolute minimal complexity using one pass
    
def solution(string):
    l = list(string)
    res = []
    for i in range(0, len(l), 2):
        # If there is a neighbor, append it then the current (swapped order relative to index i, but we are building result sequence)
        # Wait, swapping adjacent characters means "ab" -> "ba".
        # So if we have l[i] and l[i+1], result should get l[i+1] then l[i].
        res.append(l[i])

if __name__ == '__main__':
    pass
