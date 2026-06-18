def calculate_phrase_length(phrase):
    """
    Calculate the total character count of a given string using Python's built-in len().
    
    This is considered the most efficient method in standard Python as it operates 
    directly on the internal representation (bytes or unicode object) without explicit looping.
    
    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: Total character count of the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "Python 3 is awesome",
        "😀🎉"  # Multi-character emoji sequence to ensure unicode handling works correctly
    ]

    results = []
    
    print("Testing calculate_phrase_length function:")
    for phrase in test_cases:
        length = calculate_phrase_length(phrase)
        results.append((phrase, length))
        print(f"'{phrase}' -> {length} characters")