def remove_spaces_from_strings(string_list):
    """
    Takes a list of strings as input, removes all spaces from each string individually,
    and returns a new list with the modified strings.

    Args:
        string_list (list[str]): A list containing original strings that may have internal spaces.

    Returns:
        list[str]: A new list where every space character (' ') in each input string has been removed.
    
    Example:
        >>> remove_spaces_from_strings(["hello world", "foo bar baz"])
        ['helloworld', 'foobarbaz']
    """
    return [string.replace(" ", "") for string in string_list]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_input = ["hello world", "foo bar baz", "no spaces here"]

    result_output = remove_spaces_from_strings(test_input)

    print("Input list:", test_input)
    print("Output list after removing internal spaces:", result_output)