def total_string_length(string_list):
    """
    Calculates the combined length of all strings in a given list without 
    creating intermediate string objects to ensure high performance.
    
    Args:
        string_list (list[str]): A list containing zero or more string elements.
        
    Returns:
        int: The sum of lengths of all strings in the input list.

    Raises:
        TypeError: If an element in the list is not a string instance.
    """
    total_length = 0
    
    # Iterate through each item to check type and accumulate length directly
    for item in string_list:
        if isinstance(item, str):
            total_length += len(item)
        else:
            raise TypeError(f"List contains non-string element of type {type(item).__name__}")

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external dependencies or input required
    test_cases = [
        ["hello", "world"],
        [],
        ["python", "is", "fast"],
        ["a"] * 100,
        []
    ]

    for i, data in enumerate(test_cases):
        try:
            result = total_string_length(data)
            print(f"Test case {i + 1}: Input length={len(data)}, Total characters={result}")
        except TypeError as e:
            print(f"Test case {i + 1} Error: {e}")