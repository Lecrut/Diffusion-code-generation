def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        weight_pairs (list of tuples or lists): A list where each element is a pair 
                                               representing two weights, e.g., [(10, 5), (20, 8)].
    
    Yields:
        float/int: The absolute difference between the two weights in each pair.
    
    This function is memory efficient as it processes pairs one at a time without storing results.
    """
    for pair in weight_pairs:
        if len(pair) != 2:
            raise ValueError(f"Each element must be a pair of length 2, got {len(pair)}")
        w1, w2 = pair[0], pair[1]
        yield abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    samples = [
        [(5.0, 3.0), (10, 7), ('a', 'b'), (100, 98)],
        [[20, 4], [6, 6]],
    ]

    for i, pair_list in enumerate(samples):
        print(f"\nSample {i + 1}:")
        diff_generator = weight_difference_generator(pair_list)
        
        # Demonstrate the generator by iterating once (memory efficient approach)
        diffs = list(diff_generator)
        print("Differences:", [f"{d:.2f}" for d in diffs])

    # Example usage showing direct iteration without full storage if needed:
    sample_single = [(10, 5), (9, 4)]
    print("\nDirect iteration example:")
    diff_gen = weight_difference_generator(sample_single)
    
    while True:
        try:
            val = next(diff_gen)
            print(val)
        except StopIteration:
            break