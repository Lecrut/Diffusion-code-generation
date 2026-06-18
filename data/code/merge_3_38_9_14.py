def analyze_string_characters(text: str):
    """
    Analyzes a string to return unique characters and repeated characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        tuple: A tuple containing two elements:
            - set of unique characters found in the string
            - list of characters that appear more than once, maintaining order of first appearance
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> analyze_string_characters("hello")
        ({'e', 'l', 'h', 'o'}, ['h'])  # Note: exact repetition list may vary based on implementation details regarding order/stability
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) since there can be at most 26 unique lowercase English letters (assuming ASCII input).
    """
    
    # Validate input type strictly to ensure only strings are processed, as per task requirements for safety and clarity.
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    char_count = {}
    repeated_chars_ordered = []
    seen_in_repeated_list = set()  # To avoid duplicates in the output list
    
    unique_characters_set = set()
    
    for index, character in enumerate(text):
        if not isinstance(character, str) or len(character) != 1:
            continue
            
        unique_characters_set.add(character)
        
        char_count[character] += 1
        
        # Check if we have encountered this character before while counting but haven't added it to the repeated list yet.
        if char_count[character] > 1 and character not in seen_in_repeated_list:
            repeated_chars_ordered.append(character)
            seen_in_repeated_list.add(character)

    return unique_characters_set, repeated_chars_ordered

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "hello",             # Expected: Unique={'e','h','l','o'}, Repeated=['h'] (order depends on iteration)
        "aabbccdd",         # No repeated characters strictly greater than 1 if we consider unique sets, but here 'aa' repeats -> ['a'], etc.
                           # Actually based on logic: Unique={'a','b','c','d'}, Repeated=['a', 'b', 'c', 'd'] because each appears twice.
        "abc",              # No repeats expected in repeated list.
        "",                 # Empty string edge case.
    ]

    for test_input in test_cases:
        unique_set, repeated_list = analyze_string_characters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Unique Characters Set: {unique_set}")
        print(f"Repeated Characters List: {repeated_list}\n")