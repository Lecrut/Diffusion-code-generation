def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between pairs of weights.
    
    Args:
        weight_pairs (list[tuple]): A list where each element is a tuple containing two numeric values representing weights.
        
    Yields:
        float or int: The absolute difference between the first and second value in each pair.
        
    Example:
        >>> gen = weight_difference_generator([(10, 5), (20, 3)])
        >>> next(gen)
        5.0
        >>> next(gen)
        17.0
    """
    for w1, w2 in weight_pairs:
        yield abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values as a list of tuples (weight_pair_1, weight_pair_2, ...)
    samples = [
        (10.5, 4.2),
        (20, 3),
        (100, 98),
        (-5, -12)
    ]

    generator_obj = weight_difference_generator(samples)

    print("Weight differences:")
    for diff in generator_obj:
        # Ensure float formatting is consistent if needed, though Python handles mixed types naturally here.
        formatted_diff = f"{diff:.2f}" if isinstance(diff, (int, float)) else str(diff)
        print(formatted_diff)

    # Verify all items were processed without memory issues by iterating once through the generator
    count = sum(1 for _ in weight_difference_generator(samples))
    assert count == len(samples), "Generator should yield exactly one value per input pair."