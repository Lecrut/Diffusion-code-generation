def compare_sequences(seq_a: list, seq_b: list) -> str:
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences.
    
    Args:
        seq_a (list): First sequence of comparable values.
        seq_b (list): Second sequence of comparable values.
        
    Yields:
        str: Description of the relationship ('A is greater', 'B is smaller', or 'Equal').
       """
    if len(seq_a) != len(seq_b):
        raise ValueError("Both sequences must have the same length.")

    for val_a, val_b in zip(seq_a, seq_b):
        try:
            comparison = val_a > val_b
        except TypeError:
            # If values cannot be compared (e.g., mixed types), skip or handle as needed.
            continue
        
        if comparison:
            yield "A is greater"
        elif val_a < val_b:
            yield "B is smaller"
        else:
            yield "Equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    sequence_one = [10, 5, 20, 3]
    sequence_two = [8, 6, 19, 4]

    print("Comparison results:")
    result_generator = compare_sequences(sequence_one, sequence_two)
    
    for comparison_result in result_generator:
        print(comparison_result)