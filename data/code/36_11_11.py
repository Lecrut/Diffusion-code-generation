def reverse_string(s: str) -> str:
    """
    Returns a new string that is the reverse of the input string s.
    
    This implementation uses Python's built-in slicing which creates 
    an optimized copy in C, making it highly efficient for large strings.
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(n) to store the reversed result.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: A new string containing characters from 's' in reverse order.
    
    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("")
        ""
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        ("hello", "olleh"),
        ("Python is great!", "!traeg si nohtyP"),
        ("", ""),
        ("A man a plan a canal Panama!", "amanaP !nalac a napla a nam A"),
        (12345, None)  # This case will fail as expected since input must be str
    ]

    for i, (input_str, expected_output) in enumerate(test_cases):
        if isinstance(input_str, str):
            result = reverse_string(input_str)
            status = "PASS" if result == expected_output else f"FAIL: Expected '{expected_output}', got '{result}'"
            print(f"Test {i+1}: Input='{input_str}' -> Output='{result}' [{status}]")
        else:
            print(f"Test Case Skipped for index {i} (Input must be a string)")

    # Additional standalone demonstration with a large random-like string simulation
    long_string = "x" * 10000 + "y" * 5000 + "z" * 3000
    reversed_long = reverse_string(long_string)
    
    print("\nPerformance Test:")
    print(f"Input length: {len(long_string)}")
    print(f"First char of original: '{long_string[0]}' -> First char of reversed: '{reversed_long[-1]}'")