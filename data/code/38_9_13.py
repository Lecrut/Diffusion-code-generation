def analyze_string_chars(s: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.

    Args:
        s (str): The input string to analyze.

    Returns:
        tuple: A tuple containing two elements:
            - set[str]: A set of all unique characters found in the string.
            - list[str]: A list of characters that appear more than once, 
                         preserving their order of first appearance as repeated items.
    
    Example:
        analyze_string_chars("hello") -> ({'h', 'e', 'l', 'o'}, ['l'])
    """
    if not s:
        return set(), []

    # Track frequency and maintain order for duplicates
    char_count = {}
    repeated_order = []
    
    # First pass: count frequencies while tracking first occurrence of repeats
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            continue  # Already added to unique set below, skip here logic handled separately
        
        # Actually, let's do a single clean pass with collections.Counter or manual dict
        count[char] = count.get(char, 0) + 1
    
    from collections import Counter
    counts = Counter(s)
    
    unique_chars = set(counts.keys())
    
    repeated_list = []
    for char in s:
        if counts[char] > 1 and char not in repeated_list:
            repeated_list.append(char)
            
    return (unique_chars, repeated_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "hello",
        "aabbccdd",
        "programming",
        "",
        "no_dups_here"
    ]

    for test_input in test_cases:
        unique_set, repeated_list = analyze_string_chars(test_input)
        print(f"Input: '{test_input}'")
        print(f"Unique characters (set): {unique_set}")
        print(f"Repeated characters (list): {repeated_list}")
        print("-" * 20)