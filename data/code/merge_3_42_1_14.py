def build_string_from_parts(parts: list) -> str:
    """
    Joins a list of string parts with spaces as separators in O(n) time complexity.
    
    Args:
        parts (list): A list of strings to be joined.
        
    Returns:
        str: The concatenated string with parts separated by single spaces.
    """
    if not parts:
        return ""
    
    # Using join is inherently O(n) where n is the total length of all substrings,
    # as it performs a single pass to build the result list and then one final copy operation.
    return " ".join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "Is", "A"]
    result = build_string_from_parts(sample_parts)
    print(result)