def reverse_string(s: str) -> str:
    """
    Reverses a given input string efficiently using Python's slicing,
    which is both concise (Pythonic) and optimized in C implementation.
    
    Args:
        s (str): The original string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "Pythonic",
        "12345"
    ]
    
    print("Reversed strings from hard-coded samples:")
    original_string = "Reverse this string!"
    
    # Demonstrate with a single primary example as per standard practice when no args are provided
    reversed_result = reverse_string(original_string)
    print(f"Original:  {original_string}")
    print(f"Reversed:  {reversed_result}")