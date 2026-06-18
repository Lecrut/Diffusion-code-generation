def reverse_by_adjacent_swaps(s: str) -> str:
    """
    Reverses a string by repeatedly swapping adjacent characters until reversed.
    
    The algorithm simulates moving each character from its original position 
    to the end of the string one step at a time, which inherently reverses 
    the entire sequence through adjacent swaps (similar to bubble sort logic).
    
    Args:
        s (str): Input string to reverse
        
    Returns:
        str: Reversed version of input string
    """
    # Convert string to list for mutability
    chars = list(s)
    n = len(chars)
    
    # Move each character from index i to its final reversed position
    # Character at index 0 moves all the way to the end (n-1 steps of swaps)
    # Character at index 1 moves all the way to second-to-last (n-2 steps), etc.
    for i in range(n - 1):
        j = n - 1 - i  # Target position for character currently at i
        
        while j > i:
            chars[j], chars[j - 1] = chars[j - 1], chars[j]
            j -= 1
            
    return "".join(chars)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "Python Programming Challenge",
        "",
        "a"
    ]
    
    for test_input in sample_strings:
        result = reverse_by_adjacent_swaps(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'")
        assert result == test_input[::-1], f"Test failed for input '{test_input}'"