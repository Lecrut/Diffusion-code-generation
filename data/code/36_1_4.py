def reverse_string(text: str) -> str:
    """
    Returns the reversed version of the input string using slicing notation.
    
    Parameters:
        text (str): The original string to be reversed.
        
    Returns:
        str: A new string containing characters from the original in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = ["Hello, World!", "Python is great", "", "a"]
    
    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: '{sample}' -> Reversed: '{reversed_sample}'")