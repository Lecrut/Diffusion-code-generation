def reverse_sentence(sentence: str) -> str:
    """
    Reverses a given sentence by reversing its characters in place.
    
    Args:
        sentence (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Efficiently reverse the string using slicing, which is O(n) and immutable-safe for strings.
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input or external dependencies.
    samples = [
        "Hello World",
        "Python Programming",
        ""  # Edge case: empty string
    ]

    for s in samples:
        reversed_s = reverse_sentence(s)
        print(f"Original: '{s}'")
        print(f"Reversed: '{reversed_s}'\n")