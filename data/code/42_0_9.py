def concat_strings(string_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.

    Args:
        string_list (list): A list of individual strings to be joined.
        delimiter (str): The separator string used between items in the result. Defaults to ", ".

    Returns:
        str: The concatenated string with delimiters placed appropriately.
    """
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise TypeError("Input must be a list of strings.")
    
    return delimiter.join(str(item).replace('\n', '') for item in string_list)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # This block runs without user input, command-line arguments, network access, or files.
    samples = ["Hello", "World", "This", "is", "a", "test"]
    
    result_with_default = concat_strings(samples)
    print("Default delimiter (', '):")
    print(result_with_default)

    # Demonstration with a custom separator using the same logic internally via replace, 
    # though strictly speaking join is more robust than manual replacement.
    # To demonstrate functionality clearly without relying on internal state changes:
    
    sample_list_2 = ["Python", "is", "fun"]
    result_custom_sep = concat_strings(sample_list_2, delimiter=" | ")
    print("\nCustom separator (' | '):")
    print(result_custom_sep)

    # Edge case test with empty list (should return empty string without exception due to join behavior)
    sample_empty = []
    result_edge_case = concat_strings(sample_empty)
    
    # Note: The current implementation does not explicitly raise an error for empty lists, 
    # as the standard library's 'join' handles them gracefully. 
    # However, if strict validation is needed based on task constraints regarding robustness:

    sample_single = ["Single"]
    result_single_item = concat_strings(sample_single)
    
    print("\nEdge case (empty list):", repr(result_edge_case))
    print("Single item:", result_single_item)