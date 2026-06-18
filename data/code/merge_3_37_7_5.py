def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two strings directly using the + operator for maximum performance 
    in simple cases where intermediate objects need not be avoided by .join().
    
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
        
    Returns:
        str: A new combined string resulting from appending s2 to s1.
    """
    return s1 + s2

if __name__ == '__main__':
    sample_string_1 = "Hello, World!"
    sample_string_2 = "!Welcome"
    
    result_combined = combine_strings(sample_string_1, sample_string_2)
    print(f"{result_combined}")  # Output: Hello, World!!Welcome