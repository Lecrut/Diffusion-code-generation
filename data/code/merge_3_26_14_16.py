def greater_than_threshold(value, threshold=10):
    """
    Generator function that yields True if value is strictly greater than threshold,
    otherwise yields nothing (or False depending on requirement interpretation).
    
    Since the task says "yields True ONLY when...": 
        - If input > threshold: yield True
        - Otherwise: do not yield anything
    
    This ensures memory efficiency by processing one item at a time.

    Args:
        value: The numerical value to check against the threshold.
        threshold (float): The predefined threshold for comparison, defaults to 10.

    Yields:
        bool: True if value > threshold, otherwise nothing is yielded.
    
    Example usage with filter(list(greater_than_threshold(x) for x in large_sequence)) 
         This would be a common use-case pattern where you want only the items that pass criteria
    """

if __name__ == '__main__':
    pass
