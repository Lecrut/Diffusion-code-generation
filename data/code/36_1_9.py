def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string using slicing notation.
    
    Parameters:
        s (str): The original string to be reversed.
        
    Returns:
        str: A new string containing characters from the original string in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        "hello world",
        "",
        "Python is awesome!",
        "A" * 100,
        "Reverse me immediately!"
    ]

    for test_input in samples:
        reversed_output = reverse_string(test_input)
        print(f"Original:   '{test_input}'")
        print(f"Reversed:   '{reversed_output}'\n")