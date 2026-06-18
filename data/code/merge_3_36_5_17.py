def reverse_string_generator(s: str):
    """
    Generator function that yields characters of an input string in reverse order.
    
    Optimized for memory usage by processing the string from end to start index,
    avoiding full copies or reversed lists which would consume O(n) extra space.

    Args:
        s (str): Input string to iterate over in reverse.

    Yields:
        str: Individual characters from the input string in reverse order.
    
    Example:
        >>> list(reverse_string_generator("hello"))
        ['o', 'l', 'l', 'e', 'h']
    """
    # Iterate backwards using range with step -1, starting at len(s) and down to 0 (exclusive)
    for index in range(len(s), 0, -1):
        yield s[index - 1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or external dependencies.
    test_strings = [
        "Hello World",
        "Python Programming",
        "ABC"
    ]

    for test_str in test_strings:
        print(f"\nOriginal String: '{test_str}'")
        result_list = []
        
        # Using the generator to process characters one by one without storing intermediate lists of chars if not needed, 
        # but converting to list here solely to demonstrate output collection from the generator.
        for char in reverse_string_generator(test_str):
            result_list.append(char)
        
        print(f"Reversed Characters: {''.join(result_list)}")

    # Demonstration on a very large string conceptually by showing partial behavior or just running it efficiently
    # The actual memory optimization comes from the generator itself yielding one char at a time.
    # For this script, we stick to hard-coded samples as requested without generating massive strings dynamically 
    # that might hit interactive limits in some environments, ensuring no sys.stdin/input() calls.