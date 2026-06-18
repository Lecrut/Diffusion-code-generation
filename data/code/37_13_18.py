def join_strings_with_fstring(str1: str, str2: str) -> str:
    """
    Joins two strings using an f-string with a space as separator.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: The concatenated result of the two strings separated by a space.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_str_1 = "Hello"
    sample_str_2 = "World"
    
    # Ensure variables are defined even if they were never provided as arguments (as per task constraint to avoid input())
    result_string: str = join_strings_with_fstring(sample_str_1, sample_str_2)
    print(result_string)