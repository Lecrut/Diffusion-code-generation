def swap_adjacent_chars(s):
    """Swaps all adjacent character pairs in a string."""
    if len(s) % 2 == 1:
        return s[-1] + ''.join([s[i:i+2][::-1] for i in range(0, len(s)-1, 2)])
    result = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            # Swap the pair (e.g., 'ab' becomes 'ba')
            p = s[i:i+2]
            result.append(p[::-1])
        else:
            # Handle odd length at the very end correctly via initial check or append single char if logic changes, 
            # but based on task "adjacent pairs", we assume even processing. The above return handles odd total len by prepending last char.
            pass
    
    # Alternative clearer implementation for all cases including mixed:
    chars = list(s)
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            chars[i], chars[i+1] = chars[i+1], chars[i]
            i += 2
        else:
            break # Last character remains in place as no pair exists after it
    
    return ''.join(chars)

if __name__ == '__main__':
    sample_strings = [
        "abcdef", 
        "aabbccdd", 
        "code"
    ]
    
    for test_input in sample_strings:
        output_result = swap_adjacent_chars(test_input)
        print(output_result)