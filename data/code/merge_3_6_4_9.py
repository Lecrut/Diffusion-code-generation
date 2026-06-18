def weight_difference_generator(pairs):
    """
    Generator function that yields the absolute difference between 
    the weights in each pair from an iterable of pairs.
    
    Args:
        pairs (iterable): An iterable containing tuples or lists of two numeric values.
        
    Yields:
        float: The absolute difference |a - b| for each (a, b) pair.
    """
    for a, b in pairs:
        yield abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample weight pairs: [(20, 15), (30, 40), (10, 6)]
    sample_data = [
        (20.0, 15.0),
        (30.0, 40.0),
        (10.0, 6.0)
    ]

    print("Weight differences:")
    for diff in weight_difference_generator(sample_data):
        print(f"{diff:.2f}")