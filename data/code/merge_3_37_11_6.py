def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings into a single string efficiently using Python's 
    built-in string join behavior via direct concatenation which is optimized in CPython.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by appending the contents of str2 to str1.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, ensuring no user interaction or file I/O is needed.
    result = combine_strings("Hello", "World")
    print(result)