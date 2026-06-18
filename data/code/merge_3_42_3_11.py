def build_string_with_spacing(elements):
    """
    Iteratively builds a string by appending each element from an input list,
    managing necessary spacing between elements correctly.
    
    If the list is empty, returns an empty string.
    Otherwise, joins all non-empty strings with a single space separator.
    Non-string elements are converted to their string representation before joining.

    Args:
        elements (list): A list of items to be joined into a single string.

    Returns:
        str: The resulting concatenated string with spaces between elements.
    """
    if not elements:
        return ""
    
    result = []
    for item in elements:
        # Convert each element to string and append to the list of parts
        result.append(str(item))
    
    # Join all parts with a single space, handling edge cases like empty input via initial check above
    return " ".join(result)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_list = ["Hello", 123, True, None]

    output_string = build_string_with_spacing(sample_list)
    
    print(output_string)