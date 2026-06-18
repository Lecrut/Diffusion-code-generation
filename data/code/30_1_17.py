def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string using slicing.
    
    The function takes even-indexed character slices and odd-indexed 
    character slices separately, then concatenates them to achieve the swap.
    This approach avoids creating intermediate lists or explicit loops for performance.
    
    Args:
        s (str): Input string
        
    Returns:
        str: New string with adjacent pairs swapped
    """
    even_indices = s[0::2]
    odd_indices = s[1::2]
    return "".join(even + odds) if len(s) > 1 else ""

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    samples = [
        "hello",       # Expected: "hlelo"
        "abcdef",      # Expected: "adbecf"
        "",            # Expected: ""
        "ab",          # Expected: "ba"
        "a",           # Expected: "a" (single char, no swap possible)
    ]
    
    print("Input -> Output")
    for sample in samples:
        result = swap_adjacent_pairs(sample)
        print(f"{repr(sample):10} -> {repr(result)}")