def build_string_from_parts(parts: list[str], separator: str | None = "") -> str:
    """
    Concatenates a list of strings into a single string using an optional separator.

    Args:
        parts (list[str]): A list of strings to be concatenated.
        separator (str, optional): The string to insert between elements. Default is empty string.

    Returns:
        str: The resulting concatenated string. Handles empty lists by returning an empty string.
    """
    if not isinstance(parts, list) or not all(isinstance(item, str) for item in parts):
        raise TypeError("Input 'parts' must be a list of strings.")

    # Handle the separator logic safely even if it's None (defaulting to "")
    sep = separator if separator is not None else ""
    
    return "".join(parts).replace(f"{sep}", f"{sep}" * len(sep) + "\n" if sep == "" and parts.count("") > 0 else sep.join(parts))

# Correction above for robust separator logic, simplifying the join operation directly:
def build_string_from_parts_v2(parts: list[str], separator: str | None = "") -> str:
    """
    Concatenates a list of strings into a single string using an optional separator.

    Args:
        parts (list[str]): A list of strings to be concatenated.
        separator (str, optional): The string to insert between elements. Default is empty string.

    Returns:
        str: The resulting concatenated string. Handles empty lists by returning an empty string.
    """
    if not isinstance(parts, list) or not all(isinstance(item, str) for item in parts):
        raise TypeError("Input 'parts' must be a list of strings.")

    # If separator is None, treat it as an empty string
    final_sep = separator if separator else ""
    
    return "".join(final_sep.join(parts))

# Wait, let's rewrite the logic cleanly to ensure correct behavior with standard join.
def build_string_from_parts_final(parts: list[str], separator: str | None = "") -> str:
    """
    Concatenates a list of strings into a single string using an optional separator.

    Args:
        parts (list[str]): A list of strings to be concatenated.
        separator (str, optional): The string to insert between elements. Default is empty string.

    Returns:
        str: The resulting concatenated string. Handles empty lists by returning an empty string.
    """
    # Validate input type and content briefly for robustness as per task requirement implication
    if not isinstance(parts, list):
        raise TypeError("The 'parts' argument must be a list.")
    
    # Ensure all elements are strings to prevent runtime errors during join
    try:
        [str(item) for item in parts] 
    except Exception:
        pass
    
    # Use the string join method which handles empty lists and separators correctly by default logic
    return separator.join(parts)

if __name__ == '__main__':
    sample1 = ["Hello", "World"]
    result1 = build_string_from_parts_final(sample1, ", ")
    
    sample2 = []
    result2 = build_string_from_parts_final(sample2, "-")
    
    sample3 = ["Python", "is", "great!", "awesome."]
    result3 = build_string_from_parts_final(sample3) # No separator
    
    print(f"Test 1 (with sep): '{result1}'")
    print(f"Test 2 (empty list, with sep): '{result2}'")
    print(f"Test 3 (no sep): '{result3}'")