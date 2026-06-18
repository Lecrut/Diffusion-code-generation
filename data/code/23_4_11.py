def compare_sequences(seq_a, seq_b):
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences.
    
    Args:
        seq_a (iterable): First sequence of comparable items.
        seq_b (iterable): Second sequence of comparable items.
        
    Yields:
        str: Description of the relationship ('A is greater', 'B is smaller', or 'Equal') 
             for each corresponding pair, stopping at the end of either sequence.
    
    Raises:
        TypeError: If elements in sequences are not directly comparable using <, >, ==.
    """
    iterator_a = iter(seq_a)
    iterator_b = iter(seq_b)
    
    try:
        while True:
            val_a = next(iterator_a)
            val_b = next(iterator_b)
            
            if val_a < val_b:
                yield "B is smaller"
            elif val_a > val_b:
                yield "A is greater"
            else:
                yield "Equal"
    except StopIteration:
        pass

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    list_one = [10, 5, 20, 3]
    list_two = [8, 6, 19, 4]
    
    print("Comparison results:")
    result_generator = compare_sequences(list_one, list_two)
    
    for comparison in result_generator:
        print(comparison)