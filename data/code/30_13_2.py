def swap_adjacent_chars(text: str) -> str:
    """Swaps all adjacent characters in a string."""
    if len(text) < 2:
        return text
    
    chars = list(text)
    
    # Swap every pair of adjacent characters using slicing and unpacking logic implicitly via iteration
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            chars[i], chars[i+1] = chars[i+1], chars[i]
            
    return "".join(chars)

if __name__ == '__main__':
    # Sample input values (no user input required)
    sample_inputs = [
        "hello",
        "",
        "a",
        "python programming"
    ]
    
    for inp in sample_inputs:
        result = swap_adjacent_chars(inp)
        print(f'Input: "{inp}" -> Output: "{result}"')