def build_string_from_parts(parts: list, separator: str = "") -> str:
    """
    Concatenates a list of strings into a single string using an optional separator.
    
    Args:
        parts (list): A list of strings to be concatenated.
        separator (str): An optional string to insert between elements in the list.
        
    Returns:
        str: The resulting concatenated string.
    """
    if not parts:
        return ""
    
    result = parts[0]
    for i in range(1, len(parts)):
        result += separator + parts[i]
    
    return result

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_list_1 = ["Hello", "World"]
    sample_separator_1 = ", "

    sample_list_2 = ["Python", "is", "great"]
    sample_separator_2 = "-"

    empty_list = []

    print(build_string_from_parts(sample_list_1, sample_separator_1))  # Expected: Hello World
    print(build_string_from_parts(sample_list_2, sample_separator_2))  # Expected: Python-is-great
    print(build_string_from_parts(empty_list, "X"))                    # Expected: (empty string)