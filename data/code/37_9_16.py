def interleave_strings(str1: str, str2: str) -> str:
    """
    Interleaves two strings by concatenating the first string followed by 
    the second string as per the example logic provided ('hello', 'world' -> 'helloworld').
    
    The problem description states "first string is followed by the second", which implies simple concatenation.
    If a true interleaving (alternating characters) was intended, it would usually specify "interleaved character-by-character".
    Given the example: 'hello', 'world' -> 'helloworld', this confirms simple concatenation.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: A new string formed by appending str2 to the end of str1.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    s1 = "hello"
    s2 = "world"

    result = interleave_strings(s1, s2)
    
    print(f"{s1} + {s2} -> '{result}'")