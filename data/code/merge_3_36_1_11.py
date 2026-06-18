def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string using slicing notation.
    
    Args:
        s (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    test_cases = [
        ("hello", "olleh"),
        ("Python3.9", "9.3nohtyP"),
        "", 
        ("A man a plan a canal Panama!", "!amanaP lanac a !anap lafam A"),
        (12345, "54321")  # Note: This test expects input to be treated as string representation
    ]

    results = []
    
    for i, value in enumerate(test_cases):
        if isinstance(value[0], str):
            result = reverse_string(value[0])
            expected = value[1]
        else:
            # If the first element is not a string (like an int), convert to string then test logic separately 
            # However, per task requirements focusing on strings as primary input example usage below handles it specifically:
            result_str_value = str(value)
            reversed_val = reverse_string(result_str_value)