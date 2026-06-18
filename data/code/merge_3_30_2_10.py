#!/usr/bin/env python3
"""
Script to swap all adjacent character pairs in a string.

This script reads a string from standard input, swaps every pair of 
consecutive characters (e.g., "abcd" becomes "badc"), and prints the result.
If there is an odd number of characters, the last one remains unchanged.

Constraints:
- No use of input(), sys.stdin.read() for interactive prompts, or argparse required arguments.
- The main execution block uses hard-coded sample values to ensure it runs without user interaction.
"""

def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the string s and returns the new string.

    Parameters:
        s (str): Input string containing characters to be processed.

    Returns:
        str: The modified string with swapped adjacent pairs.
    
    Example:
        swap_adjacent_pairs("abcd") -> "badc"
        swap_adjacent_pairs("abcde") -> "bdcae"
    """
    chars = list(s)
    length = len(chars)

    # Iterate over the string in steps of 2 and swap pairs
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]

    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input,
    # command-line arguments, or network access.
    samples = ["hello", "abcdefg", "!@#"]

    for test_string in samples:
        result = swap_adjacent_pairs(test_string)
        print(result)