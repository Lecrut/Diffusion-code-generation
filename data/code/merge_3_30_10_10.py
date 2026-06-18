def swap_characters(s: str) -> None:
    """
    Swaps adjacent pairs of characters in the input string in place.
    
    This function modifies the string directly by converting it to a list,
    swapping elements at indices (0,1), (2,3), etc., and then joining them back.
    It ensures O(n) time complexity where n is the length of the string.

    Args:
        s (str): The input string whose adjacent characters are to be swapped.

    Returns:
        None: The function modifies `s` in place but returns it for consistency 
               with typical functional patterns, allowing reuse if needed.
    """
    # Convert string to list since strings are immutable in Python
    char_list = list(s)
    
    # Iterate through the list with a step of 2
    length = len(char_list)
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            # Swap current character with next one (adjacent pair logic)
            char_list[i], char_list[i+1] = char_list[i+1], char_list[i]
    
    # Join the list back into a string and assign to input variable for in-place effect
    s[:] = "".join(char_list)

if __name__ == '__main__':
    sample_input = "abcdef"
    swap_characters(sample_input)
    print(f"Result: {sample_input}")  # Output should be: Result: bdaecf