def compare_sequences(seq_a: list, seq_b: list):
    """
    Generator function that yields comparison results between corresponding elements 
    of two input sequences.
    
    Args:
        seq_a (list): First sequence of values.
        seq_b (list): Second sequence of values.
        
    Yields:
        str: Description of the relationship ('A is greater', 'B is smaller', or 'Equal').
    """
    # Validate that both sequences have equal length
    if len(seq_a) != len(seq_b):
        raise ValueError("Both input sequences must be of equal length.")

    for val_a, val_b in zip(seq_a, seq_b):
        if not isinstance(val_a, (int, float)) or not isinstance(val_b, (int, float)):
            # Attempt numeric conversion; fall back to direct comparison logic below
            try:
                num_a = float(val_a)
                num_b = float(val_b)
            except ValueError:
                # If strings cannot be converted and aren't already numbers, 
                # use lexicographical string comparison as a fallback behavior.
                if val_a > val_b:
                    yield "A is greater"
                elif val_a < val_b:
                    yield "B is smaller"
                else:
                    yield "Equal"
        else:
            num_a = float(val_a)
            num_b = float(val_b)

            if num_a > num_b:
                yield "A is greater"
            elif num_a < num_b:
                yield "B is smaller"
            else:
                yield "Equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sequence_one = [10, 25, -3, 4.5]
    sequence_two = [7, 25, 0, 6.5]

    print("Comparison Results:")
    results = list(compare_sequences(sequence_one, sequence_two))
    
    for result in results:
        print(result)