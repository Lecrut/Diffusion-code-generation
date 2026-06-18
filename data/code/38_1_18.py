def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set containing unique repeated letters found in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Convert to lowercase and filter only alphabetic characters for consistency
    filtered_text = ''.join(char.lower() for char in text if char.isalpha())
    
    letter_counts = {}
    repeated_letters = set()
    
    for char in filtered_text:
        count = letter_counts.get(char, 0) + 1
        letter_counts[char] = count
        
        # If a character appears more than once (second occurrence onwards), add to set
        if count > 1 and char not in repeated_letters:
            repeated_letters.add(char)

    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",           # Expected: {'h', 'l', 'o'} (case-insensitive, ignores punctuation/space)
        "A man a plan a canal Panama",  # Expected: {'a', 'n', 'p'}. Note: 'm' appears twice too. Corrected expectation below.
        "Python Programming",      # Expected: {'r', 'o'} (case-insensitive handling of 'O') -> actually 'P','y','t','h','o','n',' ','P','r','o','g','r','a','m','m','i','n','g' -> repeated: p, r, o, n, m
        "aaaa",                     # Expected: {'a'}
        "",                        # Expected: set()
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Repeated letters: {result}")
        
        # Specific correction for "A man a plan a canal Panama":
        # Lowercase + alpha only: 'amanaplanacanalpanama'
        # Counts: a->5, m->4, n->6, p->3, l->2, c->1 -> Repeated should be {'a', 'm', 'n', 'p', 'l'}
        
        print("-" * 30)