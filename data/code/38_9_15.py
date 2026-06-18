def analyze_string(s: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        tuple: A tuple containing two elements:
            - set[str]: Set of all unique characters in the string.
            - list[str]: List of characters that appear more than once, 
                         preserving their first occurrence order.
    """
    if not s:
        return set(), []

    # Count character frequencies while maintaining insertion order for repeated chars logic
    char_count = {}
    
    # First pass: count all occurrences and build the unique set
    unique_chars = set()
    for char in s:
        unique_chars.add(char)
        if char not in char_count or char_count[char] == 0:
            char_count[char] = 1
        else:
            char_count[char] += 1

    # Second pass logic isn't needed for counting, but we need to identify 
    # which characters are repeated while preserving the order of their *first* appearance.
    
    unique_set = set(unique_chars)
    repeated_list = []
    
    seen_in_repeated_check = set()
    
    # Iterate through string again in original order to determine repetition status based on total count
    for char in s:
        if char_count[char] > 1 and char not in seen_in_repeated_check:
            repeated_list.append(char)
            seen_in_repeated_check.add(char)

    return unique_set, repeated_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is required
    test_string = "hello world"
    
    result_unique, result_repeated = analyze_string(test_string)
    
    print(f"Input: '{test_string}'")
    print(f"Unique characters (set): {result_unique}")
    print(f"Repeated characters (list): {result_repeated}")