def string_segment_generator(strings: list[str], separator: str) -> generator:
    """
    Generator function that yields concatenated string segments from an input list,
    using a custom separator between each segment to save memory on very large lists.

    Args:
        strings (list): A list of strings to be processed and joined with the separator.
        separator (str): The string used as a delimiter between individual elements.

    Yields:
        str: Each element from the input list, separated by the provided separator.
    
    Example:
        >>> gen = string_segment_generator(["apple", "banana"], ", ")
        >>> next(gen)
        'apple'
        >>> next(gen)
        'banana'
    """
    for item in strings:
        yield f"{item}{separator}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    large_list = [f"segment_{i}" for i in range(10)]  # Simulates a very large list efficiently
    
    separator = ", "
    
    print("Generating string segments with custom separator:")
    generator = string_segment_generator(large_list, separator)
    
    results = []
    try:
        while True:
            result = next(generator)
            results.append(result)
            if len(results) == 3:  # Print first few for demonstration to avoid excessive output
                print('\n'.join(results))
                break
    except StopIteration:
        pass
    
    print(f"\nTotal segments generated (simulated): {len(large_list)}")