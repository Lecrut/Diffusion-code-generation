def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights 
    in each given pair from a list of tuples or lists.
    
    Args:
        weight_pairs (list): List of pairs, where each element is either 
                            a tuple/list containing two numbers representing 
                            the weight pair.
                            
    Yields:
        float/int: The absolute difference between the two weights in the current pair.
        
    Memory Efficiency:
        This function processes elements one by one without storing intermediate results,
        making it suitable for large datasets where memory usage is a concern.
    """
    for pair in weight_pairs:
        # Handle both tuple and list inputs, ensuring unpacking works correctly
        w1 = pair[0]
        w2 = pair[1]
        yield abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    samples_weight_pairs = [
        (5, 3),      # Difference: |5-3| = 2
        ('apple', 'orange'), # Assuming case-insensitive comparison for strings is not intended here; 
                            # Since task says "weight pairs", we assume numeric or comparable types.
                            # If mixed types are passed unexpectedly in sample, let's stick to numbers for clarity:
    ]

    # Correcting samples to ensure they work as weight pairs (numbers)
    correct_samples = [
        (10, 5),     # Difference: |10-5| = 5
        (2.5, 3.7),  # Difference: |2.5 - 3.7| = 1.2
        ('a', 'b'),   # This might cause issues if not numbers; let's keep only numeric samples for robustness in a "weight" context
    ]

    # Final safe sample list with only integers/floats suitable as weights
    final_samples = [
        (10, 5),     
        (2.5, 3.7),  
        (100, 98)    
    ]

    print("Generating weight differences:")
    for diff in weight_difference_generator(final_samples):
        print(f"Difference: {diff}")