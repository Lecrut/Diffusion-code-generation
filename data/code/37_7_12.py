def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings efficiently. 
    For simple concatenation without complex formatting needs (like joining lists of characters),
    direct string concatenation is the most efficient and readable approach in Python for this specific case.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: A new string formed by appending str2 to str1.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without user interaction.
    sample_str_1 = "Hello, World!"
    sample_str_2 = "Python"

    result = combine_strings(sample_str_1, sample_str_2)
    print(result)