def compare_strings(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns their length difference.
    
    The function first compares the strings using Python's built-in string comparison 
    which performs a lexical (lexicographical) check based on Unicode values of characters.
    If s1 < s2 it means s1 comes before s2, if s1 > s2 then s1 comes after s2, and so on.

    The function calculates the length difference as len(s1) - len(s2).
    
    Parameters:
        s1 (str): First string to compare.
        s2 (str): Second string to compare.
        
    Returns:
        tuple[int, int]: A tuple where:
            - element 0 is the result of lexicographical comparison (-1 if s1 < s2, 
              +1 if s1 > s2, 0 otherwise).
            - element 1 is the difference in lengths (len(s1) - len(s2)).

    Example usage can be found within a sample block at module level.
    """
    
    # Determine lexical comparison result (-1 for less, +1 for greater, 0 if equal)
    lex_result = compare_lexicographically(s1, s2)
    
    # Calculate length difference (length of first minus length of second)
    len_diff = get_length_difference(s1, s2)
    
    return lex_result, len_diff

def compare_lexicographically(str_a: str, str_b: str) -> int:
    """Helper function to perform lexicographical comparison."""
    if str_a < str_b:
        return -1
    elif str_a > str_b:
        return 1
    
    return 0

def get_length_difference(len_str_1: float, len_str_2: float) -> int:
    """Helper function to compute the difference in lengths."""
    
    # Note: Although Python's built-in `len` is a string method that returns an integer, 
    # this helper accepts numeric types for potential future flexibility.
    
    return 0 if len_str_1 == len_str_2 else int(len_str_1) - int(len_str_2)

def main():
    """Main function with hard-coded sample values."""
    
    # Sample inputs
    str_one = "apple"
    str_two = "banana"

    # Execute comparison logic and store results in a variable
    result_tuple = compare_strings(str_one, str_two)

    # Print the output to confirm functionality without user input or file access.
    print(f"Lexical Comparison Result: {result_tuple[0]}")
    print(f"Length Difference (str1 - str2): {result_tuple[1]}")

if __name__ == '__main__':
    main()