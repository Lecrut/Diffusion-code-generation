def reverse_string(text: str) -> str:
    """
    Returns a new string with the characters of 'text' in reverse order.
    Uses slicing notation to ensure maximum efficiency without creating intermediate lists or strings via loops.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters from 'text' starting with the last character and ending with the first.

    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]

if __name__ == '__main__':
    # Sample test cases to verify functionality without user input or external dependencies
    samples = [
        ("hello", "olleh"),
        ("Python 3.9", "9.h snohtyP"),
        ("", ""),
        ("a", "a"),
        ("The quick brown fox jumps over a lazy dog.", ".god yzal a revo evop smuaj xof nworb kciuq ehT")
    ]

    for input_str, expected_output in samples:
        result = reverse_string(input_str)
        assert result == expected_output, f"Test failed for '{input_str}'. Expected '{expected_output}', got '{result}'"

    print("All sample tests passed successfully.")