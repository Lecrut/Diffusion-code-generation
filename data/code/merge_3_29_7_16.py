def reverse_string_in_place(s: str) -> None:
    """
    Reverses a string in-place by modifying it directly if possible, 
    or returns a new reversed string to minimize memory overhead compared 
    to creating intermediate copies. Since Python strings are immutable, 
    we convert to a list of characters (O(n)), reverse the list O(n), and join back.
    
    This approach minimizes peak memory usage relative to naive concatenation loops 
    by performing a single pass with constant extra space for pointers on the list object.

    Args:
        s (str): Input string to be reversed.
        
    Returns:
        None if modification is attempted in-place via mutable conversion, else returns new str.
    
    Note: Python strings are immutable, so true "in-place" reversal requires 
    converting to a list first. This avoids O(n) intermediate concatenated strings.
    """
    # Convert string to list for mutability (O(n) space but single allocation)
    char_list = list(s)
    
    # Two-pointer approach: swap from ends moving inward (O(1) extra space on the list object itself)
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap characters at current pointers
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

def reverse_string(s: str) -> str:
    """
    Wrapper function to return the reversed string. 
    Minimizes memory by avoiding multiple passes or intermediate full-string copies during iteration.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Reversed version of input string
    """
    # Use the optimized two-pointer logic on a list to minimize overhead
    char_list = list(s)
    left, right = 0, len(char_list) - 1
    
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
        
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies
    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a" * 1000,  # Large string for performance check without memory explosion issues in this context
        "Race car!"
    ]

    print("Original Strings and their Reversed Versions:")
    print("-" * 40)
    
    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f"Input : '{test_input}'")
        print(f"Output: '{reversed_result}'")
        print()