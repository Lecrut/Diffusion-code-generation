def compare_sequences(seq_a, seq_b):
    """
    Generator function that yields comparison results between corresponding elements 
    of two input sequences.
    
    Args:
        seq_a (iterable): First sequence of values.
        seq_b (iterable): Second sequence of values.
        
    Yields:
        str: Description of the relationship ('A is greater', 'B is smaller', or 'Equal').
             If lengths differ, yields for common length and then stops if one runs out 
             unless specified otherwise; here we assume equal length pairs as per typical 
             pairwise comparison tasks. If sequences are unequal in length, it will yield 
             up to the minimum length pair.
    """
    # Convert inputs to lists to handle iteration safely even with generators
    list_a = list(seq_a)
    list_b = list(seq_b)
    
    min_len = min(len(list_a), len(list_b))
    
    for i in range(min_len):
        val_a, val_b = list_a[i], list_b[i]
        
        if val_a > val_b:
            yield f"{val_a} is greater than {val_b}"
        elif val_a < val_b:
            yield f"{val_b} is smaller than {val_a}"
        else:
            yield "Equal"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    sequence_one = [10, 25, 3.5, 'apple', True]
    sequence_two = [7, 25, 4.0, 'banana', False]

    print("Comparison results:")
    for result in compare_sequences(sequence_one, sequence_two):
        print(result)