import json

def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Joins a list of strings into a single string with the given delimiter placed between elements.
    
    Args:
        strings (list): A list of input strings.
        delimiter (str): The custom delimiter to place between items.
        
    Returns:
        str: A joined string with delimiters inserted between original items.
    """
    if not strings:
        return ""
    
    result = []
    for i, item in enumerate(strings):
        # Append the current item
        result.append(item)
        # Add delimiter after every item except the last one to ensure it's strictly "between"
        if i < len(strings) - 1:
            result.append(delimiter)
    
    return "".join(result)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    output_string = join_strings_with_delimiter(sample_list, custom_delim)
    
    print(f"Input: {sample_list}")
    print(f"Delimiter: '{custom_delim}'")
    print(f"Output: '{output_string}'")

# Additional test case for single element list to ensure edge cases are handled correctly.
single_element = ["hello"]
result_single = join_strings_with_delimiter(single_element, "--")
assert result_single == "hello", f"Single element failed: {result_single}"

# Test with empty list
empty_list = []
result_empty = join_strings_with_delimiter(empty_list, "@")
assert result_empty == "", f"Empty list failed: '{result_empty}'"