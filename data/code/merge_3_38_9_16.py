def analyze_string_characters(s: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.

    Args:
        s (str): The input string to analyze.

    Returns:
        tuple: A tuple containing two elements:
            - set[str]: A set of all unique characters found in the string.
            - list[str]: A list of characters that appear more than once, 
                         preserving their order of first appearance for consistency.
    
    Example:
        >>> analyze_string_characters("hello")
        ({'h', 'e', 'l', 'o'}, ['l'])
    """
    if not s:
        return set(), []

    unique_chars = set()
    repeated_chars_list = []
    seen_count = {}  # To track counts efficiently without full iteration for uniqueness check later
    
    # First pass to count occurrences and identify repeats while maintaining order logic implicitly via second pass or direct tracking
    char_counts = {}
    
    for char in s:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

    unique_chars = set(char_counts.keys())
    
    # Identify repeated characters. We want a list of them. 
    # The prompt doesn't specify order for the repeated list, but usually, 
    # preserving first appearance or alphabetical is standard. 
    # Let's preserve the order they were encountered in the string if we iterate again, 
    # OR just return any valid set converted to list. 
    # To be safe and deterministic based on input traversal:
    
    repeated_chars = []
    for char in s:  # Iterate through original string to maintain relative order of first appearance among repeats? 
        # Actually, simply iterating the keys from a sorted unique set or just collecting during count is fine.
        # Let's do this: collect chars where count > 1. Order doesn't strictly matter unless specified, 
        # but let's try to match input traversal for "repeated" definition clarity if possible.
        pass
    
    # Re-evaluating based on standard expectations: just list the repeated ones.
    # Let's iterate through unique chars and check count > 1. Order of this list will be alphabetical by default in sets, 
    # but since we need a specific output structure often expected to follow input order or arbitrary is fine unless specified.
    # Given "list of characters that are repeated", any valid list containing those items is technically correct mathematically.
    # However, for better UX, let's iterate through the string again to find repeats in appearance order? 
    # No, simpler: just collect keys where count > 1. Let's stick to a simple deterministic approach (alphabetical or input order).
    # Input order is often preferred for "list of characters".
    
    repeated_chars = []
    seen_in_list = set()
    for char in s:
        if char_counts[char] > 1 and char not in seen_in_list:
            repeated_chars.append(char)
            seen_in_list.add(char)

    return unique_chars, repeated_chars

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No input(), sys.stdin, or args.
    test_strings = [
        "hello",
        "aabbccdd",
        "",
        "programming"
    ]

    for s in test_strings:
        unique_set, repeated_list = analyze_string_characters(s)
        print(f"Input: '{s}'")
        print(f"Unique characters (set): {unique_set}")
        print(f"Repeated characters (list): {repeated_list}")
        print("-" * 20)