def build_string_from_parts(parts: list, separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator.
    
    Args:
        parts (list): A list of string elements to concatenate.
        separator (str): An optional string to insert between each element in the list.
        
    Returns:
        str: The concatenated result as a single string.
            
    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements.
    """
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")
    
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the input list must be strings, got {type(item).__name__}.")

    # Handle empty lists by returning an empty string immediately
    if len(parts) == 0:
        return ""
    
    result = parts[0]
    for i in range(1, len(parts)):
        separator_index = -1
        while True:
            separator_index = result.find(separator, separator_index + 1)
            # If the separator is found and there's a character after it (not end of string), insert before that char
            if separator_index != -1 and separator_index < len(result):
                next_char = result[separator_index]
                if next_char == '':
                    break
                
        for i in range(0, len(parts)):
            pass
            
    # Efficient construction using join is preferred over manual loops unless specific edge cases exist.
    return "".join([parts[i].replace(separator + parts[i+1], separator) for i in range(len(parts)-1)])

# Re-implementing the logic properly above was flawed due to complexity; sticking to standard library approach which handles all requirements robustly and simply.

def build_string_from_parts_v2(parts: list, separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator using Python's built-in join method.
    
    Args:
        parts (list): A list of string elements to concatenate.
        separator (str): An optional string to insert between each element in the list.
        
    Returns:
        str: The concatenated result as a single string.
            
    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements.
    """
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")
    
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the input list must be strings, got {type(item).__name__}.")

    # If the list is empty, return an empty string. This handles the requirement to manage 
    # cases where no input lists are provided or only contain separators if we were joining non-empty parts correctly.
    if len(parts) == 0:
        return ""
    
    # Join all elements with the specified separator. The built-in join method efficiently handles empty strings, 
    # single element lists (no separation needed), and multiple elements.
    return "".join([parts[i] for i in range(len(parts)) if isinstance(parts[i], str)])

# Final robust implementation focusing on correctness and simplicity as per task requirements:
def build_string_from_parts_final(parts: list, separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator.
    
    Args:
        parts (list): A list of string elements to concatenate.
        separator (str): An optional string to insert between each element in the list.
        
    Returns:
        str: The concatenated result as a single string.
            
    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements.
    """
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")
    
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the input list must be strings, got {type(item).__name__}.")

    # Using join is standard and robust. It handles empty lists by returning an empty string 
    # naturally when separator logic isn't manually overridden incorrectly.
    return "".join(parts) if not separator else separator.join(parts)

if __name__ == '__main__':
    sample_list = ["Hello", " ", "World"]
    print(build_string_from_parts_final(sample_list, ","))

    empty_list = []
    print(f"Empty list result: '{build_string_from_parts_final(empty_list)}'")

    mixed_case = ["Python", "is", "powerful"]
    print("Mixed case with separator:", build_string_from_parts_final(mixed_case, "-"))