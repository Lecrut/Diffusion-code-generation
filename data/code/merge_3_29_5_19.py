def reverse_string(s: str) -> str:
    """
    Iteratively reverses a string without using built-in reversal methods.
    
    Parameters:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Convert the immutable string into a mutable list of characters
    char_list = list(s)
    
    # Use two pointers, one at the start and one at the end
    left = 0
    right = len(char_list) - 1
    
    # Swap elements moving towards the center
    while left < right:
        # Store character from the 'left' pointer in a temporary variable
        temp = char_list[left]
        
        # Assign character at 'right' to 'left' position, then move 'left' forward and 'right' backward
        char_list[left] = char_list[right]
        
        if left != right:  # Move both pointers only if they are not the same index (avoids overwriting on odd length middle element)
            left += 1
        
        # If we haven't reached the center, move 'right' backward; otherwise stop to avoid infinite loop in even/odd cases with swapped logic above. 
        # However, simpler approach: just decrement right and increment left inside same iteration if not at exact match, but for clean iterative swap:
        
        # Re-evaluating pointer movement within the while loop condition naturally handles convergence
        
        right -= 1
    
    # Note on logic correction to ensure correctness without redundant checks above in actual implementation below.

# Corrected simple version embedded directly:
def reverse_string_fixed(s):
    char_list = list(s)
    left, right = 0, len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = ["hello", "Python", "", "a"]
    
    for text in test_cases:
        reversed_text = reverse_string_fixed(text)
        print(f"Original: '{text}' -> Reversed: '{reversed_text}'")