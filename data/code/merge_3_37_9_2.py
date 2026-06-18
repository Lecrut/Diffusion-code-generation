def interleave_strings(str1: str, str2: str) -> str:
    """
    Interleaves two strings by concatenating characters from each string in order.
    
    This function takes two input strings and returns a single new string where 
    the first character of str1 is followed by the first character of str2, then 
    the second character of str1, and so on. If one string runs out of characters, 
    the remaining characters from the other string are appended directly.
    
    Parameters:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string with characters interleaved as described above.
    """
    result = []

    # Iterate up to the length of the longer string
    max_len = max(len(str1), len(str2))

    for i in range(max_len):
        if i < len(str1):
            result.append(str1[i])
        if i < len(str2):
            result.append(str2[i])

    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    str_a = "hello"
    str_b = "world"

    output_string = interleave_strings(str_a, str_b)
    
    print(f"'{str_a}' + '{str_b}' -> '{output_string}'")