def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        weight_pairs (list of tuple or list): List containing pairs of numbers representing weights.
        
    Yields:
        float: The absolute difference between the two values in a pair.
    """
    for pair in weight_pairs:
        if len(pair) != 2:
            raise ValueError(f"Each item must be a pair (length 2), got {len(pair)}")
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        ([5.0, 3.0], [8.0, 2.0]),           # Floats with one decimal place
        ((10, 4), (7, 9)),                   # Integers
        ([[100, 99]], [[1000, 1]]),          # Nested lists for variety
    ]

    print("Weight Difference Generator Output:")
    
    for i, pair_list in enumerate(samples):
        print(f"\nSample {i + 1}:")
        
        generator = weight_difference_generator(pair_list)
        
        results = list(generator)
        
        # Display original pairs and differences side by side
        if isinstance(pair_list[0], (list, tuple)):
            for j in range(len(pair_list[0])):
                pair = pair_list[j]
                diff = results[j]
                print(f"  Pair {j}: ({pair}) -> Difference: {diff}")
        
        # Summary statistics if the sample has multiple pairs
        avg_diff = sum(results) / len(results) if results else 0
        max_diff = max(results) if results else 0
        
        print(f"\nSummary:")
        print(f"  Number of pairs processed: {len(samples)}")
        for j, pair in enumerate(pair_list):
            diff = results[j]
            print(f"    Pair {j}: ({pair}) => |{pair[0]} - {pair[1]}| = {diff}")
        
        if len(results) > 0:
            print(f"\nStatistics for this sample:")
            print(f"  Average difference: {avg_diff:.2f}")
            print(f"  Maximum difference: {max_diff}")

    # Demonstrate memory efficiency by showing generator usage without full list conversion first
    print("\n--- Memory Efficient Usage Demo ---")
    
    large_sample = [(i, i * 10) for i in range(1_000)]  # Large dataset
    
    gen_obj = weight_difference_generator(large_sample)
    
    # Process items one by one without storing all results in memory initially
    count = sum(1 for _ in gen_obj if _)
    print(f"Total pairs processed efficiently: {count}")

    final_results = list(gen_obj)  # Convert to list only after processing
    
    min_diff = min(final_results)
    max_diff = max(final_results)
    
    print(f"\nRange of differences for large dataset:")
    print(f"  Minimum difference: {min_diff:.2f}")
    print(f"  Maximum difference: {max_diff:.2f}")