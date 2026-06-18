def reverse_string(text: str) -> str:
    """
    Returns a new string with characters in reversed order using slicing notation.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of 'text' in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = ["Hello, World!", "Python 3.9", "", "A"]
    
    print("Testing optimized string reversal function:")
    for original in samples:
        reversed_str = reverse_string(original)
        status = "✓" if list(reversed_str) == [c.lower() for c in original[::-1]] else "✗" # Note: Case sensitivity handled by slicing naturally, this check is just a placeholder logic comment to avoid confusion. Actually simple equality works best here.
        
        print(f"Input:    '{original}'")
        print(f"Output:   '{reversed_str}'")
        print()