def strictly_increasing_generator(sequence):
    """
    Generator function that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise False (or None).
    
    Since the prompt says "yields True only when...", it implies yielding a boolean.
    For cases where no comparison can be made or values are equal/non-increasing,
    we yield False to maintain consistency as a binary indicator of the condition met.
    
    Args:
        sequence (iterable): An iterable of comparable elements.
        
    Yields:
        bool: True if current > previous, else False. The first element yields None 
             or False depending on interpretation; here we yield None for the first 
             item to avoid false positives, but strictly following "yields True ONLY when",
             implies other times it should not yield True. To keep output clean as booleans:
             We will yield False if condition is not met (including start).
    """
    prev = None
    
    for val in sequence:
        # On the first item, we cannot compare with a previous value strictly greater than one that doesn't exist.
        # The requirement says "True ONLY when current > previous". 
        # If it's not true (which includes start), do not yield True.
        if prev is None or val <= prev:
            # Yield False to indicate the condition was NOT met on this step.
            yield False
        else:
            yield True
        
        prev = val

if __name__ == '__main__':
    sample_sequence = [10, 5, 20, 30, 40, 35]

    print("Sequence:", sample_sequence)
    results = list(strictly_increasing_generator(sample_sequence))
    
    # Mapping the yielded values to a more readable log format for verification:
    # Index | Value      | Previous | Comparison (Val > Prev?) | Yielded?
    # 0     | 10         | None     | N/A                      | False
    # 1     | 5          | 10       | No                       | False
    # 2     | 20         | 5        | Yes (20 > 5)            | True
    # ... and so on.

    print("Output from generator:")
    for i, is_strictly_greater in enumerate(results):
        value = sample_sequence[i] if i < len(sample_sequence) else "N/A"
        prev_val = sample_sequence[i-1] if i > 0 else None
        
        status = f"{value} ({'>'} {prev_val}) -> {'True (Strictly Greater)' if is_strictly_greater else 'False'}"
        print(f"Index {i}: Value={value}, Previous={prev_val} => Status: {status}")

    # Verify the logic specifically for True yields.
    true_indices = [i for i, r in enumerate(results) if r]
    print("\nIndices where strictly greater condition was met:", true_indices)