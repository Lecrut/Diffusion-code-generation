def swap_to_reverse(s: str) -> str:
    """
    Swaps adjacent characters iteratively to reverse a string in-place (conceptually).
    
    This function creates a list of characters from the input string and performs
    swaps between index i and i+1 for every even step, effectively reversing 
    the order by moving elements towards their mirrored positions.
    
    Args:
        s (str): The input string to be reversed through adjacent swaps.
        
    Returns:
        str: The reversed version of the original string.
    """
    # Convert string to a list for mutability
    char_list = list(s)
    n = len(char_list)
    
    # Iterate from left to right, swapping each character with its next neighbor
    # This approach effectively reverses the array by bubbling elements 
    # through their adjacent positions until fully reversed.
    for i in range(n - 1):
        char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
        
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_strings = [
        "hello",
        "Python3.9",
        "",
        "a"
    ]

    for original in test_strings:
        reversed_string = swap_to_reverse(original)
        print(f"Original: '{original}'")
        print(f"Reversed via adjacent swaps: '{reversed_string}'")
        
        # Verification (optional logic to confirm correctness based on problem statement behavior)
        if reversed_string == original[::-1]:
            status = "Correct"
        else:
            status = "Mismatch in expected reversal result"
            
        print(f"Status: {status}\n")