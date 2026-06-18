import itertools

def compare_sequences(seq_a: list, seq_b: list) -> generator:
    """
    Generator that yields comparison results between pairs of values from two sequences.
    
    Args:
        seq_a (list): First sequence of comparable items.
        seq_b (list): Second sequence of comparable items. Must be the same length as seq_a.
        
    Yields:
        str: A description of the relationship ('A is greater', 'B is smaller', or 'Equal') 
             for each corresponding pair in the input sequences.
    
    Raises:
        ValueError: If the lengths of the two sequences differ.
    """
    if len(seq_a) != len(seq_b):
        raise ValueError("Both sequences must have the same length.")

    for item_a, item_b in zip(seq_a, seq_b):
        try:
            result = (item_a > item_b) - (item_a < item_b)
            
            if result == 1:
                yield "A is greater"
            elif result == -1:
                yield "B is smaller"
            else: # result == 0, meaning equal
                yield "Equal"
        except TypeError as e:
            raise ValueError(f"Incompatible types for comparison at index {seq_a.index(item_a)}: {e}")

if __name__ == '__main__':
    sample_values = [10, 25, 'apple', 3.5]
    
    # Create two sequences based on the hard-coded samples
    sequence_one = list(range(4))          # [0, 1, 2, 3]
    sequence_two = sample_values            # [10, 25, 'apple', 3.5]

    print("Comparing integers with mixed types (may result in TypeError for string comparison):")
    
    try:
        results = compare_sequences(sequence_one, sequence_two)
        
        index_counter = 0
        for res in results:
            if index_counter < len(sample_values):
                # Only process up to the length of our safe integer list (first 3 items are comparable safely as ints vs ints)
                # Actually, Python allows int > str but it returns False. It doesn't crash unless types are incompatible for ordering logic in some contexts or explicit comparison fails.
                print(f"Index {index_counter}: Value A={sequence_one[index_counter]}, Value B={sample_values[index_counter]} -> Result: {res}")
            index_counter += 1
            
    except TypeError as e:
        # This handles cases where direct comparison raises an error, though Python usually returns False for int>str.
        print(f"Comparison failed due to incompatible types: {e}")

    # A second safe example with integers only
    print("\nComparing two integer sequences:")
    seq_int_a = [50, 12, 98]
    seq_int_b = [7, 44, 3]
    
    results_safe = compare_sequences(seq_int_a, seq_int_b)
    
    for res in results_safe:
        print(f"Result: {res}")