def weight_difference_generator(pairs):
    """
    Generator function that yields the absolute difference between weights 
    in a list of (weight1, weight2) pairs. Memory efficient as it processes items one by one.
    
    Args:
        pairs (list or iterable): List/tuple of tuples where each tuple contains two numeric values representing weights.
        
    Yields:
        float: Absolute difference between the first and second element of each pair.
    """
    for weight1, weight2 in pairs:
        yield abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input() or args)
    data = [
        (50.0, 47.3),
        (100.0, 98.5),
        (25.5, 26.1),
        (30.0, 30.0),
        (75.5, 74.8)
    ]

    print("Weight differences:")
    
    # Initialize the generator and consume it in a single pass to yield results directly
    diff_gen = weight_difference_generator(data)
    
    for difference in diff_gen:
        print(difference)