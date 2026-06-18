def concatenate_strings(first: str, second: str) -> str:
    """
    Returns a new string formed by appending the second string to the first.
    
    Args:
        first (str): The initial string.
        second (str): The string to be appended.
        
    Returns:
        str: Concatenated result using f-string formatting for clarity.
    """
    return f"{first}{second}"

if __name__ == '__main__':
    sample_first = "Hello"
    sample_second = ", World!"
    
    # Hard-coded execution without user input or external dependencies
    combined_result = concatenate_strings(sample_first, sample_second)
    print(combined_result)