def find_repeated_letters(text: str) -> set:
    """
    Identifies all letters that appear more than once in the input string,
    ignoring case sensitivity but counting total occurrences regardless of case.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set containing unique repeated characters found in lowercase form.
    """
    letter_count = {}

    for char in text:
        # Only process alphabetic characters
        if char.isalpha():
            lower_char = char.lower()
            letter_count[lower_char] = letter_count.get(lower_char, 0) + 1

    return {char for char, count in letter_count.items() if count > 1}

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies.
    samples = [
        "Hello World",       # Expected repeated letters: 'l', 'o' (case-insensitive match)
        "Mississippi",       # Expected repeated letters: 'i', 's', 'p'
        "Python Programming",# Expected repeated letters: 'n', 'g', 'r', 'm', 'a', ' ', 
    ]

    for test_string in samples:
        print(f"Testing string: '{test_string}'")
        repeated = find_repeated_letters(test_string)
        
        # Sort the result set into a list and join them to make printing cleaner, 
        # but note that sets themselves are unordered. Here we sort for deterministic output.
        sorted_result = "".join(sorted(repeated)) if isinstance(repeated, str) else "".join(sorted(list(repeated)))

        print(f"Repeated letters: {sorted_result}")
        
    # Additional explicit single test case to ensure standalone execution clarity
    final_test_input = "A man a plan a canal Panama!"
    
    repeated_letters = find_repeated_letters(final_test_input)
    output_string = "".join(sorted(list(repeated_letters))) if not isinstance(output_string, str) else output_string
    
    print(f"\nFinal test case input: '{final_test_input}'")
    # Directly constructing the sorted string manually for clarity since return is a set internally.
    repeated_set_copy = find_repeated_letters(final_test_input).copy() 
    final_output_str = "".join(sorted(repeated_set_copy)) if isinstance(final_output_str, str) else None 
    
    print(f"Repeated letters in '{final_test_input}': {final_output_str}")