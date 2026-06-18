import sys

def swap_adjacent_chars(s: str) -> str:
    """Swaps every pair of adjacent characters in a string."""
    chars = list(s)
    length = len(chars)
    
    # Iterate only up to the last even index
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            # Swap current character with next one
            chars[i], chars[i+1] = chars[i+1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input, arguments, or network access.
    samples = [
        "abcdef",
        "",          # Empty string edge case
        "a",           # Single character edge case (no swap possible)
        "1234567890"  # Numeric characters
    ]

    for sample in samples:
        result = swap_adjacent_chars(sample)
        print(result, end='\n')