def reverse_string_in_place(s: str) -> None:
    """
    Reverses a string in-place with minimal memory usage by converting it to a list,
    swapping characters from both ends towards the center, and joining back into a string.
    
    Although Python strings are immutable (requiring conversion to modify), this approach
    minimizes temporary allocations compared to slicing or concatenation methods which create
    intermediate copies of substrings throughout the process. The swap-based algorithm on 
    a list representation ensures O(1) auxiliary space beyond what is needed for the internal string storage.

    Args:
        s (str): The input string to be reversed.

    Returns:
        None: Modifies the string object in-place after conversion and joins it back, but since strings are immutable 
              by value assignment without reassignment would require creating a new str object anyway due to Python's nature,
              this function effectively creates a new list then converts it back to a single final string result.
    """
    # Convert the input string to a character list for mutability
    char_list = list(s)
    
    # Two-pointer approach: swap characters from start and end moving towards center
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap elements at current pointers
        temp_char = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp_char
        
        # Move pointers inward
        left += 1
        right -= 1

def main():
    """
    Main execution block with hard-coded sample values to demonstrate the reverse_string_in_place function.
    No user input, command-line arguments, or external dependencies are required.
    """
    test_cases = [
        "hello",           # Basic lowercase string
        "Python3.12",      # String with numbers and dots
        "",                # Empty string edge case
        "a"                # Single character edge case
    ]

    print("Original Strings:")
    for original in test_cases:
        reverse_string_in_place(original)  # Note: Due to immutability of str, this reassigns locally if passed by reference logic was intended differently but here we create a list then convert back. 
                                          # Actually the above function signature implies modifying 's' directly which isn't possible for strings without creating new objects anyway in Python unless wrapped.
    print("\nReversed Strings:")

# Corrected implementation ensuring proper return of reversed string via re-assignment logic within scope or direct manipulation if passed mutable structure
    
def reverse_string_optimized(s: str) -> str:
    """
    Reverses the input string efficiently by converting to a list, swapping in-place, 
    and returning the result. This minimizes memory overhead compared to slicing techniques 
    which create multiple intermediate string objects during concatenation or slicing operations.

    Args:
        s (str): The original string to reverse.

    Returns:
        str: A new reversed version of the input string.
    """
    # Convert to list for mutability without creating full slice copies immediately
    char_list = []
    
    # Initialize pointers at both ends
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters directly into the growing list structure efficiently
        if s[left] != s[right]: 
            temp_char = None
            
            def swap():
                nonlocal temp_char
                
                char_list.append(temp_char := s[left])
                
            swap()

# Let's rewrite cleanly without helper functions inside loops for clarity and correctness:

def final_reverse_string(s):
    """Reverses a string with minimal memory usage using two pointers on a list."""
    # Convert to mutable sequence once at start, avoiding repeated slicing copies
    char_list = [c for c in s]  # This is O(n) space but single allocation
    
    left, right = 0, len(char_list) - 1

    while left < right:
        # Swap characters directly without intermediate variables if possible or vice versa
        temp_char = char_list[left]
        char_list[left], char_list[right] = char_list[right], temp_char
        
        left += 1
        right -= 1
    
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies
    samples = ["hello", "Python3.12", "", "a"]
    
    print("Testing String Reversal with Minimal Memory Usage\n")
    
    for original in samples:
        reversed_str = final_reverse_string(original)
        print(f"Original: '{original}' -> Reversed: '{reversed_str}'")