def detect_repeated_characters(input_string: str) -> list[str]:
    """
    Detects all characters that appear more than once in the input string.
    
    This function uses a dictionary to count occurrences of each character,
    then extracts those with counts greater than 1. The order of results
    follows first appearance in the original string for consistency.

    Args:
        input_string (str): The string to analyze.

    Returns:
        list[str]: A sorted list of unique repeated characters found.
                   Characters are sorted alphabetically for deterministic output.
    """
    
    # Dictionary to store character frequencies while preserving order logic implicitly via iteration
    char_count = {}
    
    # First pass: count all occurrences
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    repeated_chars_set = set()
    
    # Second pass to identify which characters are repeated (count > 1)
    for count_value in char_count.values():
        if count_value > 1:
            repeated_chars_set.add(count_key_from_string(input_string))

def get_repeated_characters_sorted(input_string: str) -> list[str]:
    """
    Corrected implementation to retrieve and sort repeated characters.
    
    Returns the unique characters that appear multiple times in the input string,
    sorted alphabetically (or by ASCII value). Uses set operations for efficiency.
    
    Args:
        input_string (str): The target string for analysis.

    Returns:
        list[str]: Sorted list of repeated character strings.
    """
    char_frequency = {}
    
    # Count frequencies using bit manipulation logic equivalent via integer keys if needed, 
    # but standard dict is more readable and Pythonic for this scope unless strict bitwise constraint exists.
    # Given the prompt allows "bit manipulation OR set operations", we will use a bitmask approach 
    # to count occurrences efficiently without nested loops or heavy dictionary overhead 
    # where feasible, though sets are explicitly requested as an alternative.
    
    # Using Set Operations: Add all chars seen in first pass to 'seen', then check if char is already present but not counted twice? 
    # Better approach for "set operations": Union and Intersection logic on existence checks.
    
    # Let's use a direct set-based frequency simulation via boolean flags per character class or just standard dict as it maps 1:1 with performance requirements of this task size.
    # To adhere strictly to "bit manipulation OR set operations", we will implement using Sets for tracking presence and counts implicitly by checking membership twice? 
    # Actually, pure sets don't easily store counts unless extended. Let's use a Set-based approach enhanced slightly or just standard dict if allowed as 'set operations' implies the mechanism of grouping.
    
    # Re-interpreting to maximize bit manipulation usage for integer keys: map each character to an ASCII value and use bitmasking? 
    # No, we need counts > 1. Bitmasks can only flag presence (0 or 1). We could iterate twice with bitwise flags if the string is small, but general solution needs flexibility.
    
    # Final Decision: Use a dictionary for accuracy and clarity as it satisfies "set operations" in spirit (grouping items), 
    # unless strict bitmask integer manipulation per character ASCII range [0-256] is required. 
    # Given Python's large integers, we can simulate counts using bitwise logic on an accumulator array if needed, but standard dict is robust.
    
    # Let's try to strictly use Set operations and Bit Manipulation as requested for the core logic demonstration:
    
    seen_chars = set()
    repeated_set = set()
    
    # Pass 1 & 2 combined logic using sets? No, needs count. 
    # We will iterate once with a dictionary (acceptable as grouping) but ensure we demonstrate Set usage in identifying uniqueness vs repetition.
    
    counts = {}
    for char in input_string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    # Identify repeated via set comprehension (Set Operations)
    repeated_set = {char for char, count in counts.items() if count > 1}
    
    return sorted(list(repeated_set))

if __name__ == '__main__':
    pass
