def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        weight_pairs (list of tuples or lists): List containing pairs of numerical values representing weights.
        
    Yields:
        float: The absolute difference between the two weights in a pair.
    """
    for pair in weight_pairs:
        if len(pair) != 2:
            raise ValueError(f"Each element must be a pair, got {len(pair)} elements.")
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_pairs = [
        (5.2, 3.8),
        (10.0, 7.5),
        (2.4, 9.1),
        (15.6, 15.6),
        (0.1, 0.9)
    ]

    print("Weight differences:")
    for diff in weight_difference_generator(sample_pairs):
        print(f"{diff:.2f}")