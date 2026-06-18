def reverse_string(s: str) -> str:
    """
    Returns a new string with the characters of the input reversed in place order logic-wise (time O(n)).
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or file access
    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a" * 100,  # Testing with a longer string for performance efficiency
        "<script>alert('xss')</script>"
    ]

    print("Input\tReverse")
    print("-" * 35)
    
    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f'{original!r}\t{reversed_str!r}')