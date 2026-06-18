def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with those at odd indices in a string.
    
    For example, if input is "abcd", output becomes "badc".
    If the length is odd (e.g., "abcde"), the last character remains unchanged 
    as there is no neighbor to swap it with on one side only within valid pairs.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with even and odd indexed characters swapped.
    """
    if not s:
        return s
    
    result = list(s)
    length = len(result)
    
    # Iterate through the first half of indices to perform swaps
    for i in range(0, (length - 1), 2):
        even_idx = i
        odd_idx = i + 1
        
        if odd_idx < length:
            result[even_idx], result[odd_idx] = result[odd_idx], result[even_idx]
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    samples = [
        "abcd",           # Even length: a<->b, c<->d -> badc
        "abcde",          # Odd length: a<->b, c<->d, e stays -> bdc ea (actually bdcea)
        "",               # Empty string
        "a",              # Single character
        "1234567890"     # Even digits with odd positions
    ]
    
    for sample in samples:
        swapped = swap_even_odd_indices(sample)
        print(f"Input: '{sample}' -> Output: '{swapped}'")