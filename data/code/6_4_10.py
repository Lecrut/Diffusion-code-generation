def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        weight_pairs (list of tuples or lists): List containing pairs of numerical values representing weights.
        
    Yields:
        float: The absolute difference between the two weights in a given pair.
    """
    for pair in weight_pairs:
        if len(pair) != 2:
            raise ValueError(f"Each element must be a list or tuple with exactly two elements, got {len(pair)}")
        yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    # Hard-coded sample values for testing the generator without user input or external dependencies.
    sample_weight_pairs = [
        (50.0, 48.5),
        (123.7, 125.9),
        ('a', 'b'),  # Non-numeric strings to demonstrate error handling if needed; currently treated as objects with __sub__ defined? 
                     # Actually, Python's subtraction on non-ints raises TypeError. Let's stick to numbers for robustness in this simple demo.
    ]

    # Re-defining sample pairs strictly with floats/ints to avoid runtime errors on subtraction of strings.
    valid_sample_pairs = [
        (10.5, 8.2),
        (200, 195.5),
        (-3.4, -7.6)
    ]

    print("Weight differences:")
    for diff in weight_difference_generator(valid_sample_pairs):
        # Formatting to two decimal places for clarity
        formatted_diff = f"{diff:.2f}" if isinstance(diff, float) else str(diff)
        print(formatted_diff)