def reverse_string(s: str) -> str:
    """
    Reverses a given input string using Python's built-in slice notation,
    which is considered the most efficient and 'Pythonic' approach.

    Parameters:
        s (str): The string to be reversed.

    Returns:
        str: A new string containing characters of `s` in reverse order.
    
    Example usage within main block:
        input_text = "Hello World" -> output will be "dlroW olleH"
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample value to demonstrate functionality without external input sources.
    sample_input = "Python is Fun!"

    reversed_result = reverse_string(sample_input)

    print("Original:", sample_input)
    print("Reversed:", reversed_result)