def reverse_string(input_str: str) -> str:
    """
    Reverses a given string using Python's built-in slicing, 
    which is efficient (O(n)) and idiomatic.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed version of the input string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction or external dependencies needed.
    samples = [
        "hello world",
        "",
        "Python scripting is fun!",
        "A man, a plan, a canal: Panama!"
    ]

    for sample in samples:
        reversed_str = reverse_string(sample)
        print(f"Original:   '{sample}'")
        print(f"Reversed:   '{reversed_str}'\n")