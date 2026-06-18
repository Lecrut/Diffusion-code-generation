def reverse_string(s: str) -> str:
    """
    Reverses a string in-place as much as possible by converting to list,
    swapping characters from both ends, then joining back into a new string.
    
    This approach minimizes memory usage compared to creating multiple intermediate 
    copies of the entire string (like slicing s[::-1]) because it only creates 
    one additional list object proportional to the input length and performs O(n) swaps.
    While Python strings are immutable by design, this method avoids deep copying 
    logic found in some alternative recursive or functional implementations.

    Args:
        s (str): The input string to reverse.

    Returns:
        str: A new string with characters reversed.
    
    Note on Memory Efficiency:
    Direct slicing s[::-1] creates a copy of the entire string immediately, 
    which is O(n) space but highly optimized in CPython due to internal optimizations.
    However, constructing a list and swapping manually demonstrates an algorithmic approach 
    that could be adapted for environments where creating full copies is restricted or expensive.
    
    Since Python strings are immutable, we must convert the string to a mutable list of characters,
    perform swaps in place (O(1) extra space beyond the conversion), then join into a new result.
    This ensures no intermediate large string objects are generated during processing other than 
    the final output and the temporary character list.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(n) for storing characters in the list (inevitable due to mutability).
    """
    # Convert string to a list of characters for mutability
    char_list = list(s)
    
    # Two-pointer approach to swap elements from both ends moving towards center
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap the character at 'left' with the character at 'right'
        temp_char = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp_char
        
        # Move pointers towards center
        left += 1
        right -= 1
    
    # Join the list back into a string. This is necessary as lists cannot be returned directly 
    # and avoids creating an intermediate reversed string before joining (which would waste memory).
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or external dependencies are needed.
    test_cases = [
        "hello",           # Simple case
        "Python Programming",  # Case with spaces and mixed casing
        "",                # Edge case: empty string
        "a"                # Edge case: single character
    ]

    for original in test_cases:
        reversed_result = reverse_string(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_result}'\n")