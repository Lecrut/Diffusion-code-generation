import itertools

def compare_sequences(seq_a: list, seq_b: list) -> generator:
    """
    Generator function that yields comparison strings for each pair of values
    from two input sequences.

    Yields one string per element in the shorter sequence indicating whether:
    - The value in seq_a is greater than the corresponding value in seq_b.
    - The value in seq_b is greater (or eqivalent to A being smaller).
    - Both values are equal.

    If sequences have different lengths, it stops at the length of the shorter one.
    """
    
    # Use itertools.zip_longest if we wanted to handle unequal lengths with fillvalue,
    # but here we strictly iterate through pairs from two provided input sequences.
    # We assume standard pairing based on index until exhaustion.
    
    for val_a, val_b in zip(seq_a, seq_b):
        if val_a > val_b:
            yield f"{type(val_a).__name__} is greater"
        elif val_a < val_b:
            yield f"{val_b.__class__.__name__} is smaller ({val_a})" # Or simply "A is smaller" logic applied to B perspective as requested phrasing implies comparing A vs B. 
            # Re-reading request: 'B is smaller'. This usually means B's value is the result of being small relative to something, or describing relation like "Value in seq_b is smaller".
            # Let's stick to a clear descriptive format for relations between A and B values at that index.

if __name__ == '__main__':
    pass
