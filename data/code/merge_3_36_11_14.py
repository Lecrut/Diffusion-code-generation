def reverse_string(s: str) -> str:
    """
    Returns a new string that is the reverse of the input string s.
    
    This implementation uses Python's slicing feature which creates an immutable 
    copy in C-level optimized memory, providing O(n) time complexity and being 
    highly efficient for large strings compared to manual character iteration loops.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: A new string containing the characters of s in reverse order.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
        >>> reverse_string("A man a plan, a canal Panama!")
        '!amanaP ,lanac a ,nalp a nam A'
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    test_cases = [
        "hello",
        "",
        "A man a plan, a canal Panama!",
        "Python is awesome.",
        "12345"
    ]

    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_str}"\n')