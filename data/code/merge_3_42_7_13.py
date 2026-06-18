def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Takes a list of strings and a custom delimiter, returning a single string
    where the delimiter is placed between every element.
    
    Args:
        strings (list[str]): The list of input strings.
        delimiter (str): The separator to place between elements.
        
    Returns:
        str: A single joined string with delimiters in between.
    """
    if not strings or all(len(s) == 0 for s in strings):
        return ""

    result = [s]
    i = 1
    while i < len(strings):
        # Insert delimiter before the next element, except after empty ones at this specific position logic is handled below. 
        # Actually, we want to join all non-empty elements but if an element IS empty string in input, it should be skipped ONLY IF ALL are empty? 
        # No, the task says "between every element". If I have ["a", "", "b"], result should likely be a + delimiter "" (which is just ) wait no.
        pass
    
    # Refined logic: Just standard join works if we treat elements as they are. 
    # But let's stick to explicit loop for clarity per request style.
    
    parts = [s for s in strings]
    res_parts = []
    i = 0
    while i < len(parts):
        res_parts.append(parts[i])

if __name__ == '__main__':
    pass
