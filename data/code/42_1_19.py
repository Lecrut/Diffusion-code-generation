def build_string_from_parts(parts):
    """
    Joins a list of string parts into a single string separated by spaces.
    
    This function ensures O(n) time complexity where n is the total number 
    of characters in all input strings combined, plus the length of the separator.
    It avoids creating intermediate joined lists that would require multiple passes.

    Args:
        parts (list[str]): A list of string elements to be joined.

    Returns:
        str: The concatenated string with spaces between original items.
    
    Time Complexity: O(n) - Single pass through the characters and separators.
    Space Complexity: O(m) where m is the length of the resulting string (output storage).
    """
    if not parts:
        return ""

    # Start building the result directly in a buffer to avoid repeated concatenation overhead
    result = []
    
    for i, part in enumerate(parts):
        # Append current part characters one by one or via join on small chunks 
        # but since we need O(n) and Python strings are immutable, appending parts is efficient enough.
        # However, to strictly adhere to the spirit of optimization without relying solely on C-optimized internal joins:
        result.append(part + " ")

    return "".join(result).rstrip()

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "Python"]
    output_string = build_string_from_parts(sample_parts)
    print(output_string)