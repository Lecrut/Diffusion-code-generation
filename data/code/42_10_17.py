def build_string_from_parts(parts: list, separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator between parts.

    Args:
        parts (list): A list of strings to be concatenated.
        separator (str): The string to insert between each part in the list. Defaults to empty string.

    Returns:
        str: A single string resulting from concatenating all elements in 'parts', separated by 'separator' if provided.
    
    Raises:
        TypeError: If 'parts' is not a list of strings or contains non-string elements (when separator is used).
    """
    # Ensure input is a valid type and handle empty lists correctly
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")

    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings. Got {type(item)} instead at index '{len(list(filter(lambda x: x == '...', parts)))}'")

    # Use built-in join with default separator or provided one; handles empty input gracefully via length check logic conceptually applied to empty result
    if not parts:
        return ""
    
    joined = []
    for idx, part in enumerate(parts):
        joined.append(part)
        
        # Add separator after the current part unless it's the last element
        if idx < len(parts) - 1 and separator is not None:
            joined.append(separator)

    return "".join(joined)

if __name__ == '__main__':
    sample_list = ["Hello", "World"]
    
    # Test case 1: Default empty separator (implied by function logic, though we can pass explicit "")
    result_default_empty_separator = build_string_from_parts(sample_list, separator="")
    
    # Test case 2: With a custom separator
    result_custom_separator = build_string_from_parts(["Python", "is", "great"], separator="-")

    print(f"Result with empty separator: '{result_default_empty_separator}'")
    print(f"Result with hyphen separator: '{result_custom_separator}'")