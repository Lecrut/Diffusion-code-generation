def reverse_string(text: str) -> str:
    """
    Reverses a given input string.
    
    Parameters:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction)
    samples = [
        "Hello, World!",
        "",
        "Python is awesome",
        "!olleH ,dlroW"  # Expected output: reverse of itself if input was already reversed logic check not needed here, just demonstration. Actually the sample below should be a normal string to show reversal effect clearly or test edge case. Let's use a simple one.
    ]

    for original in samples:
        result = reverse_string(original)
        print(f"Input: '{original}'")
        print(f"Output: '{result}'\n")