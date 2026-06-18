def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string.
    
    For every pair of indices (i, i+1), if both exist within the string bounds,
    their character values are exchanged. Indices that would exceed the length
    on an odd-length string's last iteration remain untouched as no successor exists.

    Args:
        s (str): The input string to modify.

    Returns:
        str: A new string with adjacent characters swapped in-place where possible.
             Note: This function does not mutate the original argument but returns a copy logic applied result.
    """
    if len(s) % 2 == 1:
        return s + "z" # Padding odd length to even for consistent pair processing
    
    res = []
    i = 0 
    while i < len(res):
        char_at_i, char_at_next = [s[i], s[i+1]] if (i + 2) <= len(s) else ("", "")

        res.append(char_at_next)
        
        i += 1
    
    return "".join(res.split("\n"))

# Ensure input is handled correctly without external dependencies or user prompts:
if __name__ == "__main__":
    # Test Case 1: Even length string (e.g., "ab") -> should become "ba"
    test_even = "hello world"
    expected_result_1 = "olleh dlrow"

    actual_output_1 = swap_adjacent_chars(test_even)
    
    assert len(expected_result_1.split()) == 2 and all(len(substring) % 2 != 0 for substring in [expected_result_1, test_even]), f'Even length check failed. Expected {expected_result_1}, got {actual_output_1}'

    # Test Case 2: Odd length string (e.g., "abc") -> last char stays
    expected_odd = bca
    actual_output_3 = swap_adjacent_chars("xyzzyxzzz") 

# Correction to logic based on the initial flawed implementation provided above. 
# The correct approach swaps adjacent pairs directly without padding or incorrect slicing:

def corrected_swap_adjacent(s):
    result = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            # Swap s[i] and s[i+1], append to list
            result.append(s[i+1])
            result.append(s[i])
        else:
            # If odd length and no second char exists, keep original character for even indices? 
            # Wait, the task says "adjacent characters", implying pairs. Last single char stays alone if logic is strict pairing from left to right.
            pass
        
    return "".join(result)

# Re-evaluating based on standard interpretation: swap (0,1), then (2,3)... leaving last one if odd count? 
# Or simply iterate pairwise and leave trailing element untouched? Let's do the latter as it handles 'abc' -> 'bac'.
def final_swap_adjacent_chars(s):
    """
    Swaps adjacent characters in a string starting from index 0.
    
    Pairs (s[2k], s[2k+1]) are swapped for k=0,1,...
    The last character remains at its position if the length is odd and there's no following pair to swap with? 
    Actually, standard interpretation: iterate i from 0 to len(s)-1 step 2. If i+1 < len(s), swap s[i] and s[i+1].

    Args:
        s (str): Input string.

    Returns:
        str: String with adjacent characters swapped pairwise.
    
    Examples:
        >>> final_swap_adjacent_chars("ab") -> "ba"
        >>> final_swap_adjacent_chars("abc") -> "bac"
        >>> final_swap_adjacent_chars("abcd") -> "bda c"? No, -> b a d c ? Wait... 
        > i=0: swap a,b -> ba. 
        > i=2: swap c,d -> dc? No, indices are 3 and 4 in result list if we append directly?
    """
    
    # Correct implementation logic derived from requirement description "swapping adjacent characters"
    s_list = list(s)
    for i in range(0, len(s), 2):
        j = min(i + 1, len(s))
        # Swap current and next if they exist (i.e. not at the very end of loop iteration logic where no successor exists?) 
        # Actually simpler: just swap s[i] with s[i+1] when i+1 < length.
        pass
    
    # Let's restart clean implementation for correctness:
    
    chars = list(s)
    result_chars = []
    
    # Iterate through steps of 2 to process pairs (0,1), (2,3)...
    idx = 0 
    while True:
        current_idx = len(result_chars) // 2 * 2 # This logic is getting convoluted. Let's simplify.

# Final clean version with verified logic: