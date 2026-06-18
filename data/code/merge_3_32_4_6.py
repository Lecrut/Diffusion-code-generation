def calculate_total_length(string_list):
    """
    Calculates the total combined length of all strings in a list.

    Args:
        string_list (list[str]): A list containing one or more strings.

    Returns:
        int: The sum of lengths of all strings provided as input.

    Performance Note:
        This function iterates through each string only once, performing an O(n) operation where n is the total number 
        of characters across all strings in the list. It avoids unnecessary type conversions or repeated iterations.
    """
    if not isinstance(string_list, list):
        raise TypeError("Input must be a list.")

    for item in string_list:
        if not isinstance(item, str):
            raise ValueError(f"Expected only strings in the list, found {type(item).__name__}.")

    return sum(len(s) for s in string_list)

if __name__ == '__main__':
    pass
