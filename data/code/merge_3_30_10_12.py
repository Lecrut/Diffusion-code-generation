def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in a string in place and returns it.
    
    The function modifies the input string by creating a new list of characters,
    swapping every pair (indices 0-1, 2-3, etc.), then joining them back into a string.
    This approach ensures O(n) time complexity where n is the length of the string.
    
    Parameters:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped. If the original 
             was passed as an argument, this function returns a copy modified in place logic-wise;
             note that since strings are immutable in Python, "modifying in place" strictly speaking
             means constructing and returning the result based on input modification steps.
    """
    # Convert string to list for mutability (though we'll create new elements anyway)
    chars = list(s)
    
    # Iterate over indices with step 2
    for i in range(0, len(chars), 2):
        # Check if there's a next character to swap with
        if i + 1 < len(chars):
            # Swap the current and next characters
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return ''.join(chars)

if __name__ == '__main__':
    sample_inputs = [
        "ab",
        "abcdefg",
        "",
        "a"
    ]

    for test_input in sample_inputs:
        result = swap_characters(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")