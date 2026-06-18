def append_strings(first: str, second: str) -> str:
    """
    Appends the second string to the first using an f-string.
    
    Args:
        first (str): The initial string.
        second (str): The string to be appended.
        
    Returns:
        str: A new string with the second string concatenated after the first.
    """
    return f"{first}{second}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    result = append_strings("Hello", "World")
    print(result)