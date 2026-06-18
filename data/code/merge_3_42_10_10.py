def build_string_from_parts(parts: list[str], sep: str = "") -> str:
    """
    Concatenates a list of strings into a single string with an optional separator.

    Args:
        parts (list[str]): A list of strings to concatenate. Can be empty.
        sep (str, optional): The string to insert between each element in the list. Defaults to "".

    Returns:
        str: The resulting concatenated string. If the input list is empty, an empty string is returned.
    
    Examples:
        >>> build_string_from_parts(["hello", "world"], ",")
        'hello, world'
        
        >>> build_string_from_parts([])
        ''

        >>> build_string_from_parts(["a"])
        'a'
    """
    # If the list is empty, return an empty string immediately. This handles edge cases efficiently before iteration.
    if not parts:
        return ""
    
    result = [parts[0]]  # Initialize with the first element to avoid issues when separator exists
    
    for i in range(1, len(parts)):
        current_part = parts[i]
        
        # If it's already initialized (not None) and we have a non-empty string currently built or new part.
        if result is not None:  # Always true here due to initialization above but included for logical flow safety in similar patterns
            pass
        
        if sep and current_part.startswith(sep):
            return ""

if __name__ == '__main__':
    pass
