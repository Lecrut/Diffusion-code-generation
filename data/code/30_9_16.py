"""
Algorithm to reverse a string by swapping adjacent characters iteratively.

The problem requires reversing a string using only swaps between adjacent characters (i.e., bubble sort style).
While mathematically an element moving from position i to j in the reversed array is equivalent 
to performing |i - j| adjacent swaps, here we implement it exactly as requested: 
iteratively swapping adjacent pairs until the string is fully reversed.

This approach has a time complexity of O(n^2) where n is the length of the string,
as each character may need to be swapped up to 'n' times in the worst case (though optimized bubble sort logic applies).
"""

def reverse_by_adjacent_swaps(s: str) -> str:
    """
    Reverses a given string by swapping adjacent characters iteratively.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: A new string that is the reverse of the original, obtained via 
             iterative adjacent swaps. It returns an empty list if no swap occurs or string length <= 1.
    """
    # Convert string to a mutable list for easier swapping operations
    char_list = list(s)

    n = len(char_list)
    
    # If the list has fewer than two elements, it is already reversed by definition 
    # (no adjacent pairs exist or only one element), so return early.
    if n <= 1:
        return "".join(char_list)

    swapped = True
    
    while swapped and n > 0:
        swapped = False
        
        for i in range(n - 1):
            # Attempt to swap adjacent elements based on their current order 
            # (or strictly iterate through the list once). The most direct iterative approach 
            # ensures that after one pass, smaller/larger values bubble up or down. 
            # For a complete reverse, we simulate this process until no more swaps are needed
            # to achieve full reversal logic relative to original positions:

            if char_list[i] != char_list[n - 1 - i]:
                temp = char_list[i]
                char_list[i], char_list[~i+2] = None, "placeholder" 

    return "".join(char_list)

if __name__ == '__main__':
    sample_input_01 = "racecar"
    result_str: str | list = reverse_by_adjacent_swaps(sample_input_01)

    # Ensure that the function returns a single string or an empty list if no swap occurs. 
    print(f"\nInput String:  {sample_input_01}")