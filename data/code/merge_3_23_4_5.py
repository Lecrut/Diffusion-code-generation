def compare_sequences(seq_a: list, seq_b: list) -> str:
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences.
    
    Args:
        seq_a (list): First sequence of comparable items.
        seq_b (list): Second sequence of comparable items.
        
    Yields:
        str: A string describing the relationship ('A is greater', 'B is smaller', or 'Equal') 
             for each corresponding pair, stopping at the end of either list if lengths differ.
    
    Raises:
        ValueError: If elements in a pair are not comparable using standard comparison operators.
    """
    max_len = min(len(seq_a), len(seq_b))
    
    for i in range(max_len):
        val_a, val_b = seq_a[i], seq_b[i]
        
        try:
            if val_a > val_b:
                yield f"Index {i}: A is greater ({val_a} vs {val_b})"
            elif val_a < val_b:
                yield f"Index {i}: B is smaller ({val_a} vs {val_b})"
            else:
                yield f"Index {i}: Equal ({val_a} == {val_b})"
        except TypeError as e:
            # Handle cases where comparison isn't supported (e.g., int and str)
            raise ValueError(f"Cannot compare elements at index {i}: {str(e)}") from None

    if len(seq_a) > max_len or len(seq_b) > max_len:
        remaining = "Remaining items in one sequence were not compared due to length mismatch."
        yield f"Mismatched lengths ({len(seq_a)} vs {len(seq_b)}): {remaining}"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    data_list_1 = [3, 7.5, 'apple', True]
    data_list_2 = [9, 4, 'banana', False]

    print("Comparison Results:")
    results = compare_sequences(data_list_1, data_list_2)
    
    for result in results:
        print(result)