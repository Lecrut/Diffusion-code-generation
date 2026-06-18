def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and their lengths.
    
    Returns a tuple (lexicographic_result, length_difference).
    - lexicographic_result is 0 if equal, 1 if str1 > str2, -1 otherwise.
    - length_difference is len(str1) - len(str2).

    :param str1: First string to compare.
    :param str2: Second string to compare.
    :return: A tuple containing the lexicographic comparison result and the length difference.
    """
    # Normalize strings for case-insensitive comparison if needed, 
    # but standard lex order implies ASCII/Unicode value based unless specified otherwise.
    # We'll use direct < operator for default behavior (case-sensitive).
    
    len_diff = len(str1) - len(str2)

    lexicographic_result = 0
    
    try:
        if str1 > str2:
            lexicographic_result = 1
        elif str1 < str2:
            lexicographic_result = -1
        else:
            # Lengths are equal and content is same, result remains 0.
            pass
            
    except TypeError as e:
        raise ValueError(f"Strings must be comparable for lex comparison: {str(e)}") from e

    return (lexicographic_result, len_diff)

if __name__ == '__main__':
    pass
