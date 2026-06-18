def interleave_strings(str1: str, str2: str) -> str:
    """
    Interleaves two strings such that characters from str1 appear first in order,
    followed by characters from str2 in order. This effectively concatenates them.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by placing all characters of str1 before those of str2.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str1 = 'hello'
    sample_str2 = 'world'
    
    result = interleave_strings(sample_str1, sample_str2)
    print(result)