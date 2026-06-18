def compare_sequences(seq_a: list, seq_b: list) -> str:
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences.
    
    Args:
        seq_a (list): First sequence of comparable items.
        seq_b (list): Second sequence of comparable items.
        
    Yields:
        str: A string describing the relationship ('A is greater', 'B is smaller', or 'Equal') 
             for each corresponding pair. Assumes sequences are of equal length.
    
    Raises:
        ValueError: If the input sequences have different lengths.
    """
    if len(seq_a) != len(seq_b):
        raise ValueError("Input sequences must be of equal length.")

    for val_a, val_b in zip(seq_a, seq_b):
        try:
            result = (val_a > val_b) - (val_a < val_b)
            
            if result == 1:
                yield "A is greater"
            elif result == -1:
                yield "B is smaller"
            else:
                yield "Equal"
        except TypeError as e:
            # In case items are not directly comparable (e.g., mixed types)
            raise ValueError(f"Incompatible item types for comparison at index {seq_a.index(val_a)}") from e

if __name__ == '__main__':
    sample_seq_1 = [3, 5, 2.5, 'a', 7]
    sample_seq_2 = [4, 6, 2.5, 'b', 8]

    print("Comparison Results:")
    for result in compare_sequences(sample_seq_1, sample_seq_2):
        print(result)