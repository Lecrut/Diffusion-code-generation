def calculate_weight_difference(w1: float, w2: float) -> float:
    """
    Calculate the absolute difference between two weight values efficiently.

    Args:
        w1 (float): First weight value.
        w2 (float): Second weight value.

    Returns:
        float: The absolute difference |w1 - w2|.
    """
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing; no user input or external dependencies required.
    weight_a = 50.75
    weight_b = 43.2

    result = calculate_weight_difference(weight_a, weight_b)
    print(f"The absolute difference is: {result}")