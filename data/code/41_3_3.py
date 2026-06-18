def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple with the original string, its lowercase version, 
    and its reversed case version using built-in methods.
    
    Args:
        s (str): The input string
        
    Returns:
        tuple[str, str, str]: A tuple containing (original, lowercased, reverse_cased)
    """
    # Create a list of characters where each character's case is swapped
    reversed_case_list = [char.swapcase() for char in s]
    
    return (s, s.lower(), ''.join(reversed_case_list))

if __name__ == '__main__':
    sample_string = "Hello World!"
    original, lowercased, reverse_cased = process_string(sample_string)
    print(f"Original: {original}")
    print(f"Lowercase: {lowercased}")
    print(f"Reversed Case: {reverse_cased}")