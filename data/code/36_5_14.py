def reverse_string_generator(s):
    """
    Generator function that yields characters of an input string in reverse order.
    
    Optimizes memory usage by not creating a reversed copy of the entire string,
    instead iterating backwards from the last index to the first using integer arithmetic.
    This approach is O(n) time and O(1) auxiliary space (excluding output storage).

    Args:
        s (str): The input string to be processed in reverse.

    Yields:
        str: Characters of the input string, one at a time, from last to first.

    Raises:
        TypeError: If the input is not a string.
    
    Example:
        >>> list(reverse_string_generator("hello"))
        ['o', 'l', 'l', 'e', 'h']
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string type, got {type(s).__name__}")

    length = len(s)
    
    # Iterate backwards using range with a negative step
    for i in range(length - 1, -1, -1):
        yield s[i]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "hello world",
        "",
        "a" * 10**6,  # Large string to demonstrate memory efficiency conceptually (though not fully materialized in generator)
        "Python is awesome!"
    ]

    for sample_str in test_cases:
        print(f"\nProcessing input of length {len(sample_str)}:")
        
        # Demonstrate the generator by converting it to a list immediately after yielding all items.
        reversed_chars = [char for char in reverse_string_generator(sample_str)]
        
        result_str = "".join(reversed_chars)
        print(f"Reversed output: '{result_str}'")