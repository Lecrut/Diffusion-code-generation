def append_strings(first: str, second: str) -> str:
    """
    Appends the second string to the first using an f-string.
    
    Args:
        first (str): The initial string.
        second (str): The string to be appended.
        
    Returns:
        str: A new string formed by concatenating `first` and `second`.
    """
    return f"{first}{second}"

if __name__ == '__main__':
    sample_first = "Hello, World!"
    sample_second = "This is a test."
    
    result = append_strings(sample_first, sample_second)
    print(result)