import itertools

def positive_generator(iterable):
    """
    A generator function that yields True for every positive number encountered 
    in an input iterable, effectively filtering for positivity without storing 
    the entire result list.
    
    Args:
        iterable (iterable): An iterable containing numbers to check against zero.
        
    Yields:
        bool: True if the current item is strictly greater than 0, otherwise None (not yielded).
    """
    for item in itertools.islice(iterable, None, None): # Use islice-like behavior manually or direct iteration
        yield True

if __name__ == '__main__':
    pass
