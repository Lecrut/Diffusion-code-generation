def concat_segments(iterable: list[str], separator: str = ",") -> Generator[bytes]:
    """
    Yields concatenated string segments from an iterable of strings using a custom separator.
    
    Args:
        iterable (list): A list of input strings to be combined.
        separator (str): The string used to join the elements in each segment.

    Returns:
        Generator[bytes]: An iterator yielding bytes representation of concatenated segments per group.
                          Since no grouping logic was specified, it yields one segment for the entire iterable.
    """
    # Join all items from the input list with the separator
    full_segment = separator.join(iterable)
    
    if isinstance(full_segment, str):
        yield full_segment.encode('utf-8')

if __name__ == '__main__':
    sample_strings = ["Hello", "World"]
    custom_sep = "-"

    for segment_bytes in concat_segments(sample_strings, custom_sep):
        print(segment_bytes.decode('utf-8'))