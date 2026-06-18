def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string efficiently.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with all whitespace removed.
    """
    # Using translate for optimal performance on large strings compared to list comprehension or regex
    return ''.join(text.translate(str.maketrans('', '', ' \t\n\r\f\v')))

if __name__ == '__main__':
    sample_1 = "Hello   World\tThis is a\ntest string."
    sample_2 = "\n  \t  \r  \n"

    result_1 = remove_all_spaces(sample_1)
    print(f"Input: {repr(sample_1)}")
    print(f"Output: {result_1}")

    result_2 = remove_all_spaces(sample_2)
    print(f"\nInput: {repr(sample_2)}")
    print(f"Output: '{result_2}' (Length: {len(result_2)})")