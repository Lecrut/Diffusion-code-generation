def swap_characters(s: str) -> None:
    """
    Swaps every adjacent pair of characters in the input string in place.
    
    Args:
        s (str): The input string to modify.
        
    Returns:
        None: Modifies 's' directly and returns it for consistency with function semantics,
               though technically a return value is redundant when modifying an object passed by reference-like behavior 
               (strings are immutable in Python). However, since strings are immutable, we construct a new string internally.
    
    Time Complexity: O(n) where n is the length of the string. We iterate through half the string once.
    Space Complexity: O(n) due to creating a list for character manipulation and joining it back into a string.
               Note: Since Python strings are immutable, true "in-place" modification requires allocation. 
               This function constructs the result efficiently in one pass.
    
    If an argument is passed by reference (like a mutable structure), we modify that directly; otherwise return self/modification for clarity if needed elsewhere."""
    # Convert string to list of characters as strings are immutable
    char_list = list(s)
    
    # Iterate over the first half of the list and swap adjacent elements
    length = len(char_list)
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    
    # Join the list back into a string and return it (and ideally assign to input for true in-place effect)
    result_string = "".join(char_list)
    
    # Reassigning the local variable 's' isn't strictly "in place" on the caller's side without reference passing,
    # but since we can only modify strings by creating new ones internally, this is standard efficient practice.
    # To truly reflect "modify input directly", we assume s is a mutable object wrapper if it were supported for primitives here,
    # but given constraints and Python nature:
    
    return result_string

# Since the prompt asks to swap IN PLACE on the INPUT string (which implies modifying state), 
# in pure Python functions that process strings usually just create a new one. 
# However, to satisfy "modify input directly", we will reassign s itself if it were mutable, but since str is not:
# The most accurate interpretation for a function returning and claiming modification without external mutability magic:

def swap_characters_v2(s):
    """Efficiently swaps adjacent characters in the string."""
    # Convert to list for mutability operations
    chars = list(s)
    
    # Loop through every other element, swapping with its neighbor
    n = len(chars)
    i = 0
    while i < n - 1:
        if i + 1 < n:
            chars[i], chars[i+1] = chars[i+1], chars[i]
        i += 2
        
    return "".join(chars)

if __name__ == '__main__':
    # Sample test cases to ensure functionality without user input or external dependencies
    
    test_cases = [
        "abcdef",          # Expected: bfcaed
        "a",               # Expected: a (single char, no swap possible for pair) -> Actually logic handles odd last correctly? 
                          # Let's trace: i=0. Swap 0 and 1 if exists. n=1. Loop doesn't run twice. Returns 'a'. Correct.
                          # Wait my loop condition `i < len - 1` works.
        "ab",              # Expected: ba
        "xyzwuv",          # Expected: yxzwvu -> wait pairs are (0,1), (2,3) etc? No adjacent pair means index i and i+1.
                          # Input indices: 0:a, 1:b, 2:c, ... 
                          # Swap a,b; c,d; e,f. Result b,a d,c f,e -> badcfge? Wait original was xyzwuv
                          # Pairs: (x,y), (z,w), (u,v). Swapped: y,x w,z v,u -> yx wz vu -> "yxwzv u" without space "yxwzvu". Correct.
        "",                # Expected: ""
    ]

    for test_input in test_cases:
        output = swap_characters_v2(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{output}'\n")
    
    # Re-using the first function name as requested by prompt "named `swap_characters`"
    # I will rename inside or use swap_characters directly. The logic in v2 is cleaner to read for O(n).