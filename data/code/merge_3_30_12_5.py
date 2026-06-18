import sys

def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    Example: "abcd" -> "bdac", "hello" -> "ehllo" (last char remains if odd length)
    
    Args:
        s (str): Input string
        
    Returns:
        str: String with swapped pairs
    """
    # Use list for mutability, then join. O(n) time complexity.
    chars = list(s)
    n = len(chars)
    
    # Swap in steps of 2
    i = 0
    while i < n - 1:
        if i + 1 < n:
            chars[i], chars[i+1] = chars[i+1], chars[i]
        i += 2
        
    return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    samples = [
        "abcd",
        "hello world",
        "",
        "a",
        "1234567890"
    ]

    for sample in samples:
        result = swap_adjacent_pairs(sample)
        print(result)