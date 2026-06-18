def compare_sequences(seq_a: list, seq_b: list) -> str:
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences.
    
    Args:
        seq_a (list): First sequence of comparable values.
        seq_b (list): Second sequence of comparable values.
        
    Yields:
        str: A message indicating the relationship ('A is greater', 'B is smaller', or 'Equal') 
             for each corresponding pair. If sequences differ in length, it stops at the end of the shorter one.
    """
    # Ensure we don't iterate beyond the shortest list to avoid index errors
    min_len = len(seq_a) if len(seq_a) < len(seq_b) else len(seq_b)
    
    for i in range(min_len):
        val_a, val_b = seq_a[i], seq_b[i]
        
        # Determine relationship based on value comparison
        try:
            if val_a > val_b:
                yield f"A is greater"
            elif val_b > val_a:
                yield "B is smaller"
            else:
                yield "Equal"
        except TypeError:
            # In case values are not directly comparable (e.g., mixed types)
            pass

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    list_a = [10, 5, 20, 'apple', 3.14]
    list_b = [8, 6, 20, 'banana', 3.14]

    print("Comparison Results:")
    
    # Iterate through the generator and collect results for display
    comparison_results = compare_sequences(list_a, list_b)
    
    count = 1
    try:
        while True:
            result = next(comparison_results)
            print(f"Pair {count}: {result}")
            count += 1
    except StopIteration:
        pass
    
    # Note: If sequences had different lengths, the generator would stop 
    # at the end of the shorter sequence automatically.