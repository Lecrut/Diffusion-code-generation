def contains_zero(iterable):
    """
    Generator function that yields True if any number in an iterable list is zero, 
    and False otherwise after checking all elements.
    
    Optimized for memory efficiency by processing the input iterably without loading it entirely into a separate structure.
    Note: Since this must yield exactly once (either True or False), we iterate through the input to find if any element is 0.
    If found, we yield True and stop. Otherwise, after exhausting the iterator, we yield False.

    Args:
        iterable: An iterable of numbers.

    Yields:
        bool: True if a zero exists in the iterable; otherwise yields once with False.
    
    Example usage (not shown here as per task constraints): 
        list(contains_zero([1, 2, 3])) -> [False]
        list(contains_zero([0, -5, 10])) -> [True]
    """
    for item in iterable:
        if item == 0:
            yield True
            return
    
    # If the loop completes without finding zero, we haven't yielded yet.
    # We must yield False exactly once to satisfy "yields ... otherwise".
    yield False

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_cases = [
        ([1, 2, 3], False),
        ([0, -5, 10], True),
        ([-1, -2, -3], False),
        ([4.0, 8.0, 0.0], True),
        ([]), # Edge case: empty list should yield [False]
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = list(contains_zero(input_data))
        status = "PASS" if result == [expected] else "FAIL"
        print(f"Test {i+1}: Input={input_data}, Expected=[{expected}], Result={[result]}, Status={status}")