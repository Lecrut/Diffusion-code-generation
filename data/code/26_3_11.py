def yield_greater_than(iterator, threshold):
    """
    Generator that yields True whenever an iterated value is greater than a predefined threshold.
    
    This function consumes elements from the provided iterable one by one (memory efficient),
    and outputs 'True' if the current element exceeds the given threshold; otherwise, it does nothing for that iteration.

    :param iterator: An input iterable object (e.g., list, generator).
    :param threshold: A numeric value representing the cutoff limit.
    """
    for item in iterator:
        # Check condition and yield result immediately to avoid storing all items in memory
        if isinstance(item, (int, float)): 
            if item > threshold:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values with no user input or external dependencies.
    data_list = [10, 25, 30, -5, 45, 80]
    THRESHOLD_VALUE = 20
    
    results = yield_greater_than(data_list.copy(), THRESHOLD_VALUE)
    
    for result in results:
        print(result if isinstance(result, bool) else str(bool(int(result))))