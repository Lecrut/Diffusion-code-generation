def compare_sequences(seq_a: list, seq_b: list) -> generator:
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences.

    Args:
        seq_a (list): First sequence of comparable items.
        seq_b (list): Second sequence of comparable items.

    Yields:
        str: A string describing the relationship ('A is greater', 'B is smaller', or 'Equal') 
             for each corresponding pair in the sequences. Stops if one sequence runs out.
    
    Raises:
        ValueError: If elements at a specific index are not comparable using standard comparison operators.
    """
    max_len = min(len(seq_a), len(seq_b))

    # Ensure we can iterate up to the length of the shorter list without error on indices
    for i in range(max_len):
        val_a = seq_a[i]
        val_b = seq_b[i]

        try:
            if val_a > val_b:
                yield "A is greater"
            elif val_a < val_b:
                yield "B is smaller"
            else:
                yield "Equal"
        except TypeError as e:
            # If comparison fails (e.g., comparing string and int), stop yielding to avoid infinite loop or complex error handling in simple cases.
            raise ValueError(f"Incompatible types for comparison at index {i}: cannot compare '{val_a}' with '{val_b}'.") from e

    if len(seq_a) > max_len:
        # If seq_a is longer, we could choose to stop here (as per standard zip behavior in logic usually implied by "pairs") 
        # or continue. The task implies pairs, so stopping at the shortest length is safer for generic types.
        pass

if __name__ == '__main__':
    sample_seq_a = [10, 25, 'apple', True]
    sample_seq_b = [3, 26, 'banana', False]

    print("Comparison Results:")
    try:
        for result in compare_sequences(sample_seq_a, sample_seq_b):
            print(result)
    except ValueError as ve:
        # In case of incompatible types like string vs int comparison which might vary by Python version or specific objects, 
        # though standard python allows mixed type comparisons sometimes (e.g. '2' > 1), we handle the explicit error if it occurs.
        print(f"Error encountered during iteration at index {ve.args[0].split(':')[1]}: {ve}")