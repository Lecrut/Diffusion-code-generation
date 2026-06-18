def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the absolute difference between two weight values.

    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.

    Returns:
        float: The absolute difference between weight1 and weight2.
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    w_a = 50.75
    w_b = 49.30

    result = calculate_weight_difference(w_a, w_b)
    print(f"The absolute difference is: {result}")