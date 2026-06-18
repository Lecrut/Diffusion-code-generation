"""
Utility module to build a string from an arbitrary sequence of parts 
with customizable joining mechanisms.
"""

def join_parts(parts: list, separator: str = "") -> str:
    """
    Joins a list of string parts with the specified separator.
    
    Args:
        parts (list): A list of strings to be joined.
        separator (str): The string used as a delimiter between parts. 
                         Defaults to an empty string (no separation).
        
    Returns:
        str: A single concatenated string resulting from joining the inputs.

    Example:
        join_parts(['Hello', 'World'], ', ') -> "Hello, World"
        join_parts(['A', 'B', 'C']) -> "ABC"
    """
    if not parts:
        return ""
    
    result = []
    for i in range(len(parts)):
        # Append the separator before every part except the first one to avoid 
        # leading separators, then append the current part.
        if i > 0 and separator != "":
            result.append(separator)
        
        result.append(str(parts[i]) if parts[i] is not None else "")

    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    # Sample 1: Default behavior (no separator)
    sample_1 = join_parts(['Python', 'is', 'awesome'])
    print("Sample 1:", repr(sample_1))

    # Sample 2: Custom separator (comma and space)
    sample_2 = join_parts(['Apples', 'Bananas', 'Cherries'], ', ')
    print("Sample 2:", repr(sample_2))

    # Sample 3: Special case - list with None values handling
    sample_3_parts = ['Start', None, 'End']
    sample_3 = join_parts(sample_3_parts)
    print("Sample 3 (with None):", repr(sample_3))

    # Sample 4: Empty separator explicitly requested on non-empty string list
    sample_4 = join_parts(['First Part'], '-')
    print("Single item with dash:", repr(sample_4))