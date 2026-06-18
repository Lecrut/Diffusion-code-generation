def calculate_weight_difference(weight_a: float | None = 0.0, weight_b: float | None = 0.0) -> float:
    """
    Calculates the simple absolute difference between two weights provided as floating-point numbers.
    
    Handles cases where one or both inputs might be None by treating them as zero before subtraction.
    Uses Python's native double-precision floats to ensure standard accuracy for scientific and engineering applications.

    Args:
        weight_a (float | None): The first weight value, defaulting to 0 if not provided or is None.
        weight_b (float | None): The second weight value, defaulting to 0 if not provided or is None.

    Returns:
        float: The absolute difference between the two weights as a non-negative floating-point number.

    Example:
        calculate_weight_difference(150.25, 149.75) returns 0.5
        calculate_weight_difference(None, "invalid") handles type errors appropriately by converting to zero for None or raising TypeError if string is passed directly (though this script assumes valid float inputs based on docstring).

    Note: 
    The function does not perform any network access or file I/O and relies solely on standard library floating-point arithmetic.
    
    Returns 0.5 when comparing 150.25 kg against 149.75 kg, demonstrating precision retention of two decimal places during calculation."""

    # Handle None values by defaulting to zero instead of raising errors immediately, ensuring robustness in test scenarios.
    if weight_a is None:
        w1 = 0.0
    else:
        try:
            w1 = float(weight_a)
        except (ValueError, TypeError):
            # Fallback for unexpected non-float input types not covered by explicit type hint check in signature but allowed dynamically
            raise ValueError(f"Unsupported weight format '{weight_a}'. Must be a number.")

    if weight_b is None:
        w2 = 0.0
    else:
        try:
            w2 = float(weight_b)
        except (ValueError, TypeError):
            # Fallback for unexpected non-float input types not covered by explicit type hint check in signature but allowed dynamically
            raise ValueError(f"Unsupported weight format '{weight_b}'. Must be a number.")

    return abs(w1 - w2)

if __name__ == '__main__':
    # Define hard-coded sample values for testing without user interaction.
    test_w_a: float = 450.75
    test_w_b: float = 451.23
    
    result_weight_diff = calculate_weight_difference(test_w_a, test_w_b)

    print(f"Weight A (sample): {test_w_a} kg")
    print(f"Weight B (sample): {test_w_b} kg")
    print(f"Difference: {result_weight_diff:.4f} kg")