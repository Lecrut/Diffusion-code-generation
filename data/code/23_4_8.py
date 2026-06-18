def compare_sequences(a_seq, b_seq):
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences a_seq and b_seq.

    Args:
        a_seq (iterable): First sequence of comparable items.
        b_seq (iterable): Second sequence of comparable items. Must match length to a_seq ideally, but the generator handles iteration safely up to the shortest iterable.

    Yields:
        str: Comparison result string ('A is greater', 'B is smaller', or 'Equal').
    
    Raises:
        TypeError: If inputs are not iterables.
    """
    if not hasattr(a_seq, '__iter__') or not hasattr(b_seq, '__iter__'):
        raise TypeError("Both arguments must be iterable.")

    a_iter = iter(a_seq)
    b_iter = iter(b_seq)

    while True:
        try:
            item_a = next(a_iter)
            item_b = next(b_iter)
            
            if item_a > item_b:
                yield "A is greater"
            elif item_b > item_a:
                yield "B is smaller"
            else:
                yield "Equal"
        except StopIteration:
            # Both iterators exhausted at the same time (or one ran out and we stop)
            break

if __name__ == '__main__':
    sample_list_a = [3, 10, 5, 2]
    sample_list_b = [8, 9, 4, 6]

    print("Comparison Results:")
    for result in compare_sequences(sample_list_a, sample_list_b):
        print(result)