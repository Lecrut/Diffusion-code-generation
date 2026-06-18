import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped pairs of characters. If the length is odd,
             the last character remains unchanged.
    """
    result_list = list(s)
    n = len(result_list)
    
    # Iterate through the string in steps of 2 starting from index 0 to n-1 (exclusive) and step by 2
    for i in range(0, n - 1 + ((n % 2 != 0),)): 
        if i < n:
            # Swap characters at indices i and i+1 if the second exists within bounds.
            # However, since we are stepping by 2 (i.e., i=0, i=2...), checking i+1 is safe for even length strings,
            # but to be strictly correct and avoid index errors on odd lengths without conditional logic inside loop:
            if i + 1 < n:
                result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]

    return "".join(result_list)

def main():
    """
    Reads a string from standard input (simulated via hard-coded sample), swaps adjacent characters, and prints the result.
    No user interaction or command-line arguments are required.
    """
    # Hard-coded sample values to ensure standalone execution without external inputs.
    test_strings = [
        "abcdef",   # Even length: ab->ba, cd->dc, ef->fe => ba d c fe -> b a d c f e -> badcfedc? Wait logic check below
        "abcde"     # Odd length: last char stays same. abc->bac, de->ed. Result: bac ed
    ]

    for test_str in test_strings:
        output = swap_adjacent_chars(test_str)
        print(output)

if __name__ == '__main__':
    main()