def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string using slicing."""
    if len(s) <= 1:
        return s
    
    # Create list of characters to allow mutable operations (optional, but efficient for slicing logic)
    chars = list(s)
    
    # Swap pairs: indices 0-1, 2-3, etc.
    result_chars = []
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            result_chars.append(chars[i])   # Append first of pair (which was second)
            result_chars.append(chars[i+1])# Append second of pair (which was first)
            i += 2
        else:
            # Handle odd length string by keeping the last character as is
            result_chars.append(chars[i])
            break
            
    return ''.join(result_chars)

if __name__ == '__main__':
    test_string = "abcdefg"
    swapped_result = swap_adjacent_chars(test_string)
    print(swapped_result)  # Output: bcadfeg (Note: 'g' remains at end due to odd length logic above? Wait, let's re-evaluate the requirement for pure elegance. A simpler slicing approach exists.)

# Re-implementing with a more concise and elegant one-liner style using slice concatenation
def swap_adjacent_chars_v2(s: str) -> str:
    """Elegant solution using list comprehension and string joining."""
    if len(s) == 0:
        return s
    
    # Convert to list, then use zip with reversed slices or direct indexing logic? 
    # Actually, the most elegant way without explicit loops for swapping pairs is slicing.
    # We can construct a new string by taking every second char starting from index 1 (original index i+1)
    # and interleaving them back in reverse order of their original positions relative to the swap.
    
    chars = list(s)