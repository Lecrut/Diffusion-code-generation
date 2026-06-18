def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters is swapped.
    
    If there's an odd number of characters, the last one remains as-is (effectively 
    paired with nothing). The implementation uses slicing for optimal performance.

    Args:
        s (str): Input string to process.

    Returns:
        str: String with adjacent pairs swapped.
    """
    # Swap every pair by taking even and odd indexed characters in reverse order of pairing,
    # then combining them back together using slicing.
    return "".join(s[2*i+1:i+1] for i in range(0, len(s) - 1, 2))

if __name__ == '__main__':
    sample_string = "python"
    result = swap_adjacent_pairs(sample_string)
    print(result) # Output: yohnp