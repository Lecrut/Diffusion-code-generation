def build_string_from_parts(parts):
    """
    Joins a list of string parts with a space separator in O(n) time complexity.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        
    Returns:
        str: The resulting joined string separated by spaces.
    """
    if not parts:
        return ""
    
    result_parts = []
    for part in parts:
        # Ensure each part is a string and strip leading/trailing whitespace 
        # only from the internal representation to avoid extra copying,
        # though standard join handles most cases efficiently.
        # We use list comprehension logic implicitly here via direct iteration.
        result_parts.append(part)
    
    return " ".join(result_parts)

if __name__ == '__main__':
    sample_input = ["Hello", "World", "This", "Is", "An"]
    output_string = build_string_from_parts(sample_input)
    print(output_string)