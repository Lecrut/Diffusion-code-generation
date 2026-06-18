def concat_generator(strings_iterable: list[str], separator: str) -> generator:
    """
    Generator function that yields concatenated string segments from an iterable of strings,
    using a custom separator between each segment.
    
    Args:
        strings_iterable (list): An iterable containing individual strings to concatenate.
        separator (str): The string used as the delimiter between segments.
        
    Yields:
        str: A single concatenated string formed by joining all input elements with the separator.

    Example:
        >>> list(concat_generator(['a', 'b'], '-')) 
        ['ab-']  # Note: Implementation joins everything at once based on typical "concatenated segments" interpretation,
                # but if distinct chunks are needed per call, adjust logic below to yield one result total.
    """
    joined_string = separator.join(strings_iterable)
    yield joined_string

if __name__ == '__main__':
    sample_strings = ['hello', 'world']
    custom_sep = '-'

    # Generate and collect results for demonstration without external input
    result_list = list(concat_generator(sample_strings, custom_sep))

    print("Concatenated segments:")
    if result_list:
        print(result_list[0])  # Prints the single combined string with separator inside it based on join logic above.
                                # If intent was to yield one full joined string per call as a segment list element, this holds true.