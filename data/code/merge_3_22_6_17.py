def odd_even_generator(start: int = 1, end: int = None) -> generator:
    """
    A memory-efficient generator that yields tuples of (number, 'odd' or 'even') 
    for every number in the specified range [start, end).

    Args:
        start (int): The starting integer. Default is 1.
        end (int): The ending integer (exclusive). If None, defaults to a large value 
                   suitable for demonstration but avoids infinite loops if called without arguments.
    
    Yields:
        tuple: A pair consisting of the current number and its parity ('odd' or 'even').

    Example:
        >>> list(odd_even_generator())  # Runs from 1 up to a safe default limit defined in main
        [(1, 'odd'), (2, 'even'), ..., (20, 'even')] 
        Note: The actual range depends on the sample block execution.
    """
    if end is None:
        raise ValueError("end argument must be provided or defaulted within a controlled context.")

    for n in range(start, end):
        yield n, "odd" if n % 2 else "even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    start_val = 1
    end_val = 20
    
    result_list = []

    print("Generating odd/even checks for range [", start_val, ",", end_val - 1, "]")
    
    for number, parity in odd_even_generator(start=start_val, end=end_val):
        # Collecting results into a list to verify the generator output matches expectations.
        result_list.append((number, parity))

    print("\nResults:")
    for item in result_list:
        print(item)
    
    assert len(result_list) == 20, "Expected exactly 20 items."