def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple with (original string, lowercase version, reversed case version).
    
    Args:
        s (str): The input string to process.
        
    Returns:
        tuple[str, str, str]: A tuple containing the original string, 
                              its lowercased form, and its characters in reverse order.
    """
    return s, s.lower(), ''.join(reversed(s))

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = process_string(sample_input)
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Reversed Case: {result[2]}")