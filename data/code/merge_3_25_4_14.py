def contains_zero(iterable):
    """
    Generator function that yields True if any number in an iterable list is zero, 
    and False otherwise after checking all elements.
    
    Optimized for memory efficiency by yielding immediately upon finding a zero 
    or exhausting the iterator without finding one (yielding False only once at the end).

    Args:
        iterable (iterable): An iterable sequence of numbers to check.

    Yields:
        bool: True if any element is 0, otherwise yields False after iteration completes.
    
    Examples:
        >>> list(contains_zero([1, 2]))
        [False]
        >>> list(contains_zero([1, 0, 3]))
        [True]
    """
    for item in iterable:
        if item == 0:
            yield True
            return
    
    # If no zero is found after iterating through all items
    yield False

if __name__ == '__main__':
    sample_lists = [
        [],                    # Empty list -> False
        [1, 2],                # No zeros -> False
        [0],                   # Single zero -> True
        [-5, -3, 0, 7],       # Zero present -> True
        [float('inf'), float('-inf')], # Non-zero numbers (including infinities) -> False
    ]

    for i, test_list in enumerate(sample_lists):
        result = list(contains_zero(test_list))
        print(f"Input: {test_list}")
        print(f"Output: {result}\n")