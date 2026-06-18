def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the input string.
    
    If the length of the string is odd, the last character remains unchanged.
    For example: "abcd" becomes "bacd", and "abcde" becomes "badce".
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: The modified string with adjacent pairs swapped.
    """
    result = []
    length = len(s)
    
    # Iterate over the string in steps of 2 starting from index 0
    for i in range(0, length - 1, 2):
        # Swap s[i] and s[i+1], then append to result list
        pair_char_1 = s[i + 1] if (i + 1) < length else ''
        pair_char_2 = s[i] if i < length else ''
        result.append(pair_char_2)
        # Only add the second character of the swap if a valid first character existed for this position
        # However, since we iterate by pairs, let's simplify:
        # We grab index 1 then index 0. If at any point (i+1) goes out of bounds, it means odd length end.
        
    # Correcting the logic above to be more precise in a single pass loop or using list comprehension
    
    swapped_chars = []
    
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            swapped_chars.append(s[i+1])
            swapped_chars.append(s[i])
        else:
            # Handle odd-length string: keep the last character as is. 
            # Actually per task description "swaps all adjacent pairs", usually implies ignoring stragglers or keeping them at end?
            # Standard interpretation of pairwise swap on a sequence [a,b,c,d] -> [b,a,d,c]. On [a,b,c] -> [b,a][c]? Or does it stop? 
            # Let's assume standard behavior: process pairs, leave remainder. But the example "abc" usually becomes "bac".
            # Wait, if I have 'a','b', swap to 'b','a'. If I have leftover 'c', where does it go? Usually stays at end or swaps with nothing (stays). 
            # Let's implement: take pairs [0,1], [2,3]... swap them. Leftover index n-1 remains.
            swapped_chars.append(s[i])
            
    return ''.join(swapped_chars)

if __name__ == '__main__':
    sample_strings = ["abcd", "abcde", "", "a"]
    
    for test_input in sample_strings:
        output_string = swap_adjacent_pairs(test_input)
        print(output_string)