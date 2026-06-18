def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        weight_pairs (list of tuples/lists): List containing pairs of numbers representing weights.
        
    Yields:
        float or int: The absolute difference between the two weights in a pair.
    """
    for pair in weight_pairs:
        if len(pair) >= 2:
            diff = abs(pair[0] - pair[1])
            yield diff

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network access needed)
    sample_data = [
        (5.0, 3.2),
        (10, 7),
        (2.5, 2.5),
        (100, 98.6),
        (42, 37),
    ]

    print("Weight Differences:")
    for diff in weight_difference_generator(sample_data):
        print(f"Difference: {diff}")