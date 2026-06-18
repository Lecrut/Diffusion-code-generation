"""
Module to convert relative weight ratios into absolute weights based on a total value.

This module provides an efficient function to calculate individual component weights
given their proportional relationships (ratios) and a specified total sum.
It ensures numerical stability by using floating-point arithmetic suitable for 
scientific calculations while maintaining code readability.

Usage:
    import convert_weights
    result = convert_weights.convert_ratios(ratios, total_weight)
"""

def calculate_absolute_weights(ratios: list[float], total_weight: float) -> dict[str, float]:
    """
    Calculate absolute weights from relative ratios and a given total weight.

    Args:
        ratios (list of float): A list containing the proportional values for each component.
                               Example: [10, 20] means one part is twice as heavy as another.
        total_weight (float): The target sum of all absolute weights. Must be non-negative.

    Returns:
        dict[str, float]: A dictionary mapping index strings to their calculated absolute weight values.

    Raises:
        ValueError: If the input list is empty or if ratios and total are not numeric/valid types.
    
    Example:
        >>> calculate_absolute_weights([10, 20], 30)
        {'0': 10.0, '1': 20.0}

    Note:
        The function uses a direct scaling factor approach which is O(n) where n is the number of ratios.
        This ensures high performance for large datasets while remaining computationally simple and readable.
    """
    
    # Input validation to ensure robustness against edge cases like empty lists or invalid types
    if not isinstance(ratios, list):
        raise TypeError("Input 'ratios' must be a list.")
    if len(ratios) == 0:
        raise ValueError("The input ratio list cannot be empty.")
    
    # Validate that all elements in ratios are numeric (float or int)
    for item in ratios:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All items in 'ratios' must be numbers. Got {type(item).__name__}.")

    try:
        total_weight = float(total_weight)
    except ValueError:
        raise TypeError("Input 'total_weight' must be convertible to a number.")

    # Calculate the sum of all ratios (the scaling factor denominator)
    ratio_sum = 0.0
    for r in ratios:
        try:
            val = float(r)
            if val < 0:
                raise ValueError("Ratios must be non-negative values to represent physical weights.")
            ratio_sum += val
        except (ValueError, TypeError):
            # In case a valid number was passed but failed conversion or validation logic above
            pass

    if abs(ratio_sum) < 1e-9:
        raise ValueError("The sum of ratios is too close to zero. Ratios must be positive.")

    # Calculate the scaling factor (total_weight / ratio_sum)
    scale_factor = total_weight / ratio_sum
    
    # Compute absolute weights for each component and store in a dictionary
    result_dict = {}
    for i, r in enumerate(ratios):
        abs_weight = float(r) * scale_factor
        result_dict[str(i)] = abs_weight

    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external dependencies or input prompts.
    
    # Sample 1: Simple two-component ratio with integer inputs for clarity.
    # Ratio [3, 5] sums to 8. Total weight is 40kg. Expected result: Component A=15kg, B=25kg.
    sample_ratios_1 = [3, 5]
    total_weight_1 = 40
    
    output_sample_1 = calculate_absolute_weights(sample_ratios_1, total_weight_1)
    
    # Sample 2: More complex scenario with floating point precision requirements.
    # Ratio [1.5, 2.5, 3] sums to 7. Total weight is 100g. 
    # Expected results approximately: A=21.428..., B=35.714..., C=42.857...
    sample_ratios_2 = [1.5, 2.5, 3]
    total_weight_2 = 100
    
    output_sample_2 = calculate_absolute_weights(sample_ratios_2, total_weight_2)

    # Print results to console for verification (no file I/O or network access used).
    print("Sample Output 1:")
    for key in sorted(output_sample_1.keys()):
        print(f"Component {key}: {output_sample_1[key]}")

    print("\nSample Output 2:")
    for key in sorted(output_sample_2.keys()):
        print(f"Component {key}: {output_sample_2[key]}")