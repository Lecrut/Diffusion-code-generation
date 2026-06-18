def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all pairs of characters swapped.
        
    Time Complexity: O(n), where n is the length of the string, as we iterate through it once.
    Space Complexity: O(1) excluding the space required for the output string and character storage during swap.
    
    Example:
        Input: "abcdef" -> Output: "bacdef" (swaps a<->b, c<->d, e<->f? Wait, example says 0 with 1, 2 with 3 etc.)
        Correction based on prompt description "swap index 0 with 1, 2 with 3":
        Input: "abcdefg" -> Output: "bacdefg"? No. 
        Let's trace carefully: indices (0,1), (2,3), (4,5)...
        String s = "abcde"
        i=0 swap(0,1) -> 'b' 'a' ...
        i=2 swap(2,3) -> c is at 2, d is at 3. Swap them? 
        Actually the prompt says: swaps every pair of characters (e.g., swap index 0 with 1, 2 with 3).
        This implies we are swapping s[0] and s[1], then s[2] and s[3]. It does not imply a single pass modification where subsequent indices shift. 
        However, since strings in Python are immutable, the standard approach is to build a new list of characters or use slicing.
        
        Let's re-read: "swaps every pair... e.g., swap index 0 with 1, 2 with 3".
        Does this mean simultaneous swaps? Or sequential? 
        Usually in these problems, it means partition the string into chunks of size 2 and reverse each chunk.
        
        Example logic for "abcdef":
        Chunk 1: 'ab' -> reversed is 'ba'
        Chunk 2: 'cd' -> reversed is 'dc'
        Result: 'badc...' wait, if length is odd?
        Input: "abc" -> pairs (0,1) and index 2 left alone. 
        Swap s[0] and s[1]: ba c. Output "bac".
        
        Implementation using list comprehension for clarity and efficiency in Python.
    """
    # Convert string to a list of characters since strings are immutable
    char_list = list(s)
    
    # Iterate through the list with step 2, swapping elements at i and i+1 if they exist
    n = len(char_list)
    for i in range(0, n - 1, 2):
        j = i + 1
        char_list[i], char_list[j] = char_list[j], char_list[i]
    
    # Join the list back into a string and return
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    test_cases = [
        "abcdef",      # Expected: badcfe (swap ab->ba, cd->dc? Wait. Let's re-evaluate the example logic.)
                      # Prompt says: swap index 0 with 1, 2 with 3... 
                      # If input is "abcde": indices are 0:a, 1:b, 2:c, 3:d, 4:e.
                      # Swap (0,1) -> b a c d e? No, that's just swapping positions in the list.
                      # But if we do it sequentially on an immutable string without creating intermediate copies for each step:
                      # Step 1: swap s[0],s[1] => "bacde" (if modified in place)
                      # Step 2: swap s[2],s[3] of original or current? 
                      # Usually, these problems imply partitioning the string into non-overlapping pairs.
                      # Pair 1: indices 0 and 1 -> reverse them.
                      # Pair 2: indices 2 and 3 -> reverse them.
                      # So "abcdef" becomes "badcfe". 
                      # Let's check my logic above again.
                      # My code does exactly this: iterates i=0, swaps list[0] and list[1]. Then i=2, swaps list[2] and list[3].
                      # Since we are swapping in the same list structure sequentially but indices don't overlap (step 2), 
                      # it effectively reverses every chunk of size 2.
    ]

    for test_input in test_cases:
        result = reverse_adjacent_swaps(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")