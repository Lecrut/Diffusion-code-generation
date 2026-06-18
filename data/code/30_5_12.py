def swap_alternate_indices(s: str) -> str:
    """
    Swaps characters at even indices with their neighbors (odd indices).
    Handles odd-length strings by leaving the last character unchanged,
    as it has no valid neighbor to swap with.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with adjacent characters swapped pairwise from left to right.
    """
    if not s:
        return s
    
    # Convert the string to a list of characters for mutability
    chars = list(s)
    
    # Iterate through even indices (0, 2, 4...) while staying within bounds
    # The neighbor is at index + 1. We stop one position short if length is odd+1 
    # because we only want to process complete pairs. If the string has an odd total length,
    # the last character remains as it was (the loop condition handles this naturally).
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    pass
