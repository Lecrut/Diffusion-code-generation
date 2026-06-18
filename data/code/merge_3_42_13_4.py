def concat_generator(strings_list: list[str], separator: str) -> generator:
    """
    Generator function that yields concatenated string segments from an input list,
    using a custom separator between each segment to avoid building large strings in memory.

    Args:
        strings_list (list): List of strings to concatenate.
        separator (str): String to insert between consecutive elements.

    Yields:
        str: Concatenated segments from the input list with separators applied incrementally.
    
    Example usage demonstrates efficient handling for very large lists by yielding 
    chunks rather than constructing a single massive string in memory.
    """
    if not strings_list:
        return
    
    # Yield first segment without separator prefix
    yield strings_list[0]

    current_index = 1
    while current_index < len(strings_list):
        next_segment = strings_list[current_index]
        
        # Yields the separator followed by the new string for each subsequent element
        if not isinstance(separator, str) or not isinstance(next_segment, str):
            raise TypeError("Separator and segments must be strings.")

        yield f"{separator}{next_segment}"
    
    current_index += 1

if __name__ == '__main__':
    # Hard-coded sample values for demonstration. 
    # Simulates processing a very large list efficiently without loading everything into memory at once.
    sample_large_list = [f"Item_{i:05d}_Description_" + "x" * (10**6) for i in range(1, 2)]

    separator_char = "|"

    # Generator object created but not fully consumed here to show the structure works without side effects.
    result_gen = concat_generator(sample_large_list, separator_char)
    
    print("Generator initialized successfully.")
    print(f"Sample input length: {len(sample_large_list)}")
    print(f"Separator used: '{separator_char}'")

    # Demonstrate yielding behavior with the first few items if needed for testing logic flow.
    try:
        count = 0
        while True:
            chunk = next(result_gen)
            count += 1
            if count >= 2: 
                break
        
        print(f"\nFirst yielded chunks:")
        # Since the generator yields individual segments based on our logic above, we show how it might be used.
        # In a real large list scenario, this would loop through all items one by one efficiently.
    except StopIteration:
        pass
    
    # Note: For actual concatenation of multiple chunks into a final result (if desired later), 
    # the caller can collect yielded values as needed without memory spikes on the generator itself.