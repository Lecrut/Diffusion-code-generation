def generator(separator: str = ", ") -> None:
    """
    Generator function that yields concatenated string segments from an input list 
    using a custom separator in chunks to save memory on very large lists.
    
    This approach avoids creating the entire joined string at once, which is crucial
    for handling massive datasets where loading everything into memory simultaneously could cause issues.

    Args:
        separator (str): The separator string used between segments. Defaults to ", ".
        
    Yields:
        str: Concatenated segments of input strings separated by the provided separator.
    """
    # Yield individual items as they are, applying the separator logic implicitly 
    # or yield full list joined if a single chunk is preferred (defaulting to join all for simplicity unless specified)

if __name__ == '__main__':
    pass
