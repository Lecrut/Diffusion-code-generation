def generate_weight_diffs(weight_pairs):
    """
    Generator function that yields the weight difference (second - first) 
    for each pair in a list of tuples.
    
    Args:
        weight_pairs (list[tuple]): A list where each element is a tuple (w1, w2).
        
    Yields:
        float/int: The calculated difference (w2 - w1) for each pair.
    """
    for w1, w2 in weight_pairs:
        yield w2 - w1

if __name__ == '__main__':
    # Hard-coded sample values as required lists of pairs
    samples = [
        (50, 60),   # Difference: 10
        (80, 95),   # Difference: 15
        (20.5, 35.7),  # Float difference: 15.2
        (100, 40)    # Negative difference: -60
    ]

    print("Weight Differences:")