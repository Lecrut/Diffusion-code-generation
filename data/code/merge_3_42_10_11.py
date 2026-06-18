def build_string_from_parts(parts: list[str], sep: str = '') -> str:
    """
    Concatenates a list of strings into a single string with an optional separator.

    Args:
        parts (list[str]): A list of individual string components.
        sep (str, optional): The string to insert between each component in the list.
                            Defaults to empty string (no separation).

    Returns:
        str: A single concatenated string formed by joining all elements from `parts` with `sep`.

    Example:
        >>> build_string_from_parts(['a', 'b'])
        'ab'
        >>> build_string_from_parts(['hello', 'world'], sep=' ')
        'hello world'
        >>> build_string_from_parts([])
        ''
        >>> build_string_from_parts([], sep='-')
        '-'  # Note: Separator is included as there are no items to separate, but logically empty join should be ''. Re-evaluating logic below.
    """
    # If the list of parts is empty, return an empty string regardless of separator preference.
    if not parts:
        return ""
    
    result = []
    for i in range(len(parts)):
        # Append part immediately or after a potential previous join (manual loop style)
        # Using standard library's str.join logic which handles separators correctly even on empty lists 
        # by returning an empty string. However, implementing manually to ensure robustness as per task constraints:
        if i == 0:
            result.append(parts[i])
        else:
            result.append(sep + parts[i])
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    samples = [
        (['apple', 'banana'], ', '),
        (['hello', 'world!', '?'], ''),
        ([], '-'),
        (['single'], ','),
        ['', '', ''],
    ]

    print("Testing build_string_from_parts function:\n")
    
    for i, (input_data, separator) in enumerate(samples):
        try:
            output = build_string_from_parts(input_data, separator)
            status = "SUCCESS" if isinstance(output, str) else "ERROR"
            
            # Format input representation to avoid printing raw list objects unnecessarily complexly
            formatted_input = f"{input_data!r} (sep={separator!r})"
            
            print(f"Iteration {i + 1}:")
            print(f"Input: {formatted_input}")
            print(f"Output: \"{output}\"")
            print(f"Status: {status}\n")
        except Exception as e:
            formatted_error = f"{e}"
            print(f"Iteration Error:")
            print(f"Input: {input_data!r} (sep={separator!r})")
            print(f"Error Traceback/Message:\n{formatted_error}")