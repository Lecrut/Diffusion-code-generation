def yield_concatenated(iterable: list[str], separator: str = "") -> None:
    """
    Generator function that yields concatenated string segments from an iterable of strings,
    using a custom separator between each segment.

    Args:
        iterable (list): An iterable containing strings to be joined.
        separator (str): The string used as the delimiter between items in the list.

    Yields:
        str: A single concatenated string formed by joining all input segments with the specified separator.
    
    Example usage:
        >>> result = ''.join(yield_concatenated(['a', 'b', 'c'], '-'))
        # Note: This example is illustrative of how to consume the generator, 
        # but yield_concatenated itself yields one string total per call if consumed fully.
        """
    joined_string = separator.join(iterable)
    yield joined_string

if __name__ == '__main__':
    sample_strings = ['Hello', 'World']
    custom_sep = ', '

    # Create the generator object
    gen_obj = yield_concatenated(sample_strings, custom_sep)

    # Consume and print the result from the generator
    for segment in gen_obj:
        print(segment)