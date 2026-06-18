def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two input strings into a single string.

    Args:
        str1 (str): The first string argument.
        str2 (str): The second string argument.

    Returns:
        str: The concatenated result of the two strings.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str_1 = "Hello, World!"
    sample_str_2 = "Python is great."
    result = combine_strings(sample_str_1, sample_str_2)
    print(result)