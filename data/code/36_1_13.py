def reverse_string(s: str) -> str:
    """
    Returns a new string with characters in reversed order using slicing notation.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello",
        "",
        "a",
        "Python programming demo!",
        12345,  # This will be treated as a string representation in Python
    ]

    results = []
    
    for test_input in test_cases:
        try:
            result = reverse_string(str(test_input))
            results.append(f"Input: '{test_input}' -> Output: '{result}'")
        except Exception as e:
            results.append(f"Error processing input {test_input}: {e}")

    for res in results:
        print(res)