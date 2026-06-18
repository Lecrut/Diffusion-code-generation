def interleave_strings(first_string: str, second_string: str) -> str:
    """
    Returns a new string formed by concatenating first_string followed by second_string.
    
    Args:
        first_string (str): The initial string to be interleaved.
        second_string (str): The subsequent string to be interleaved.
        
    Returns:
        str: A combined string from both inputs concatenated in order.
    """
    return f"{first_string}{second_string}"

if __name__ == '__main__':
    sample_first = 'hello'
    sample_second = 'world'
    
    result_interleave = interleave_strings(sample_first, sample_second)
    print(result_interleave)