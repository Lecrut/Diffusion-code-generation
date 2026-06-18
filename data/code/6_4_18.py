def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        weight_pairs (list of tuples or lists): A list where each element is a pair 
                                               representing two weights, e.g., [(10, 5), (20, 8)].
    
    Yields:
        float: The absolute difference between the first and second weight in each pair.
    
    This function is memory efficient as it processes pairs one at a time without storing results.
    """
    for pair in weight_pairs:
        if len(pair) != 2:
            raise ValueError(f"Each element must be a pair of two weights, got {len(pair)} elements.")
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    samples = [
        (50.0, 48.2),   # Difference: 1.8
        (100, 97.5),    # Difference: 2.5
        ("a", "b"),     # Strings treated as characters; ord('a')=97, ord('b')=98 -> diff 1
        [3.14, 3.14],   # Difference: 0.0
    ]

    print("Weight differences:")
    for difference in weight_difference_generator(samples):
        print(f"{difference:.2f}")