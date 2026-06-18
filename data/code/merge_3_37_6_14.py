def append_strings(first: str, second: str) -> str:
    """
    Returns a new string formed by appending 'second' to 'first'.
    
    Args:
        first (str): The initial string.
        second (str): The string to be appended.
        
    Returns:
        str: A concatenated string using f-string syntax for clarity.
    """
    return f"{first}{second}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    result = append_strings("Hello", "World")
    print(result)  # Expected output: HelloWorld