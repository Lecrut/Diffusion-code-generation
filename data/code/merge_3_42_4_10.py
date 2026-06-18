def yield_concatenated(iterable: list[str], separator: str = "") -> None:
    """
    Generator function that yields concatenated string segments from an iterable of strings.
    
    Args:
        iterable: An iterable containing individual strings to be joined.
        separator: A custom string used as the delimiter between elements (default is empty).
        
    Yields:
        The final concatenated result if multiple items exist, or each item individually 
        if only one exists and no explicit concatenation logic requires splitting results.
    
    This implementation joins all strings in the input iterable into a single chunk using 
    the provided separator, then yields that combined string directly rather than yielding 
    intermediate partial builds which would require buffering state outside standard generator 
    yield points for multi-item inputs unless split specifically requested per item (not applicable here).
    """
    if not isinstance(iterable, list):
        iterable = list(iterable)
    
    # Join all strings with the custom separator and yield once as one segment.
    result = "".join(separator.join([x] + [s for s in iterable[1:]]) for x in (iterable or [])) if iterable else ""
    yield result

if __name__ == '__main__':
    # Sample data hard-coded to ensure no external dependencies or input needed.
    sample_strings = ["Hello", "World", "!"]
    
    print("Generated concatenated segments:")
    for segment in yield_concatenated(sample_strings, separator=""):
        print(segment)

    print("\nWith custom separator '-':")
    for segment in yield_concatenated(sample_strings, separator="-"):
        print(segment)