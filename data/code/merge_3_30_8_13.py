"""
Module to swap adjacent characters in a string.

This module provides functionality to reverse every two consecutive characters in an input string,
handling strings of both even and odd lengths gracefully. If there is an unpaired character at the end
of the string (odd length), it remains unchanged after its preceding pair has been swapped.
"""

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every adjacent pair of characters in the given string.

    The function processes the input two characters at a time, swapping them for each complete pair found.
    If the string length is odd, the last character stays as it is because there is no partner to swap with.
    
    Args:
        s (str): The input string containing alphanumeric or other characters.

    Returns:
        str: A new string where adjacent pairs of original characters are swapped. Original trailing 
             single character remains in place if the length was odd.

    Examples:
        >>> swap_adjacent_chars("ab")
        'ba'
        
        >>> swap_adjacent_chars("abc")
        'bac'
        
        >>> swap_adjacent_chars("")
        ''
    """
    # Convert string to list for mutability, then iterate in steps of 2
    chars = list(s)
    
    result_chars = []
    
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            # Swap current and next character
            temp = chars[i]
            chars[i] = chars[i+1]
            chars[i+1] = temp
            result_chars.extend(chars[i:i+2])
            i += 2
        else:
            # Handle odd length case - append single remaining char if any
            result_chars.append(chars[i])
            break
            
    return "".join(result_chars)

if __name__ == '__main__':
    """Run hardcoded test cases without external input or dependencies."""
    
    print("Test Case 1: Even Length String")
    even_test_input = "abcd"
    expected_even_output = "bacd"
    actual_even_output = swap_adjacent_chars(even_test_input)
    
    assert actual_even_output == expected_even_output, f"\nTest Failed:\nExpected '{expected_even_output}'\nGot:  {actual_even_output}"
    print(f"Inp:     \"{even_test_input}\"")
    print(f"Output:  \"{actual_even_output}\" - PASSED\n")

    
    print("Test Case 2: Odd Length String (Non-empty)")
    odd_test_input = "abcde"
    expected_odd_output = "bacd e" # Note the space is not in string, just formatting below
    
    actual_odd_output = swap_adjacent_chars(odd_test_input)
    
    assert actual_odd_output == expected_odd_output, f"\nTest Failed:\nExpected '{expected_odd_output}'\nGot:  {actual_even_output}"
    
    print(f"Inp:     \"{odd_test_input}\"")
    print(f"Output:  \"{actual_odd_output}\" - PASSED\n")

    
    # Correction for the previous test case assertion variable reference bug and logic clarity
    
    assert actual_odd_output == "baced", f"\nTest Failed:\nExpected 'baced'\nGot:  {actual_odd_output}"
    print(f"Corrected Output Check:\nInp:     \"{odd_test_input}\"")