def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string.
    
    This function uses a list comprehension to build a new string efficiently by iterating
    over each character and including it only if its Unicode category is not 'Zs' (space separator),
    which covers spaces, tabs, form feeds, line separators, paragraph separators, and other 
    whitespace characters defined in the Unicode standard. This approach avoids multiple passes 
    or regex overhead for optimal performance on large strings.

    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with all whitespace removed.
    """
    return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    samples = [
        "Hello World",
        "\t\tNew Line\nHere",
        "   Multiple   Spaces   And  Tabs \nAnd Newlines ",
        "",
        "NoSpacesAtAll"
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f"Input: {repr(sample)}")
        print(f"Output: {repr(result)}\n")