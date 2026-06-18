def yield_concatenated_segments(strings: list[str], separator: str = " ") -> str:
    """
    Generator function that yields concatenated string segments from an input list of strings,
    using a custom separator. This approach is memory-efficient as it processes the list 
    item by item without creating intermediate joined lists for very large inputs.

    Args:
        strings (list[str]): A list of strings to be processed and yielded.
        separator (str): The string used to join individual segments before yielding.

    Yields:
        str: Each segment as a concatenated result with the specified separator, 
             or None if an empty input is provided.
    
    Note: For extremely large lists where even joining all at once consumes too much memory,
            this generator can be combined with external processing that reads chunks of data.
            However, since we are given the full list as input (which itself requires loading),
            true streaming over disk would require a different file-based approach not applicable here.

    Example:
        >>> result = [s for s in yield_concatenated_segments(["a", "b", "c"], sep="-")]
        ['a', 'a-b', 'a-b-c'] (if accumulating) or individual joins depending on logic below.
        
        The implementation below yields the cumulative join up to that point if desired, 
        but strictly following "concatenated string segments" implies joining specific subsets.
        Given ambiguity in "segments", this function will yield the full joined string of all inputs 
        after each iteration (cumulative), which is a common pattern for streaming aggregation.
        
        If distinct non-overlapping segmentations were needed, additional parameters would be required.
    """
    
    # Handle empty list case immediately to avoid yielding None or garbage
    if not strings:
        return

    current_segment = ""
    
    for item in strings:
        # Start fresh with the first item (no leading separator)
        if len(current_segment) == 0:
            current_segment = item
        else:
            current_segment += separator + item
        
        # Yield the accumulated segment up to this point
        yield current_segment

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    sample_data = ["Hello", "World", "This", "Is", "A", "Test"]
    
    print("Processing large list segments...")
    
    results = []
    for segment in yield_concatenated_segments(sample_data, separator=" -"):
        results.append(segment)
        
    # Demonstrate the output
    if results:
        final_output = "\n".join(results)
        print("\nGenerated Segments:")
        print(final_output)