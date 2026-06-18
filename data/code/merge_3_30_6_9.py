def swap_adjacent(s: str) -> str:
    """Swap adjacent characters in a string."""
    chars = list(s)
    result_chars = []
    
    # Process pairs of two or single character at end
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            result_chars.append(chars[i])
            result_chars.append(chars[i+1])
            i += 2
        else:
            # Handle odd length string by appending the last character alone (or swap with imaginary)
            # Based on standard "swap adjacent" logic, usually means pair-by-pair. 
            # If strict pairwise without truncation for odds: append as is.
            result_chars.append(chars[i])
            i += 1
    
    return "".join(result_chars)

if __name__ == '__main__':
    sample_input = "abcdef"
    output = swap_adjacent(sample_input)
    print(output) # Output: bacdef (swapped a-b, c-d, e-f? Wait logic check needed below)
    
    # Correction in logic above to ensure proper swapping order for pairs.
    # Let's rewrite the function clearly inside this block if needed or fix definition.
    pass

# Re-implementation with correct swap logic inline to be safe and concise:
def swap_adjacent_correct(s):
    chars = list(s)
    res = []
    i = 0
    while i < len(chars) - 1:
        # Swap current and next, then append both? 
        # No, standard interpretation: take pair (a,b), make it (b,a). Move to next.
        # If length is odd, last char stays or handled separately. Let's assume pairs only.
        
        res.append(chars[i+1])  # Swap order: second comes first in the new pair? 
                                # Usually "swap adjacent" means position i and i+1 exchange values.
                                # So 'ab' -> 'ba'.
        res.append(chars[i])
        i += 2
    
    if len(s) % 2 == 1:
        res.append(chars[-1] if chars else '') 
    
    return "".join(res)

# Actually, the cleanest logic without explicit while loop for brevity:
def swap_adjacent_v2(s):
    # Use zip to group by two and reverse each pair? 
    # No, simple iteration is most readable. But let's try list comp if possible.
    chars = s
    swapped_chars = []
    
    idx = 0
    while True:
        if idx >= len(chars): break
        
        first = chars[idx]
        
        if idx + 1 < len(chars):
            second = chars[idx+1]
            # Append swapped order
            swapped_chars.append(second) 
            swapped_chars.append(first)
            idx += 2
        else:
            # Odd length, append last char as is (cannot swap fully with next) OR treat as pair?
            # Assuming standard behavior where odd ends are preserved or ignored in pairs.
            swapped_chars.append(first)
            break
            
    return "".join(swapped_chars)

if __name__ == '__main__':
    test_str = "abcdef"
    print(swap_adjacent_v2(test_str))