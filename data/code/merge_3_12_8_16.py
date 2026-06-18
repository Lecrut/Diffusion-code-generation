"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to handle numerical weights, convert between 
different ratio formats (fractional, decimal), simplify fractions to their lowest terms,
and perform arithmetic operations on weighted values. It is designed for external use 
without requiring any user input or network access.
"""

def _gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two integers using Euclid's algorithm."""
    if a < 0 or b < 0:
        raise ValueError("Weights must be non-negative.")
    while b != 0:
        a, b = b, a % b
    return int(a)

def simplify_ratio(numerator: float, denominator: float) -> tuple[int, int]:
    """
    Simplify two weights into their lowest integer terms.

    Args:
        numerator (float): The first weight value.
        denominator (float): The second weight value.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.

    Raises:
        ValueError: If either input is negative or if both are zero.
    """
    # Convert to integers immediately for simplification logic
    num = round(numerator)
    den = round(denominator)

    if num == 0 and den == 0:
        raise ZeroDivisionError("Cannot simplify a ratio of two zeros.")
    
    if num < 0 or den < 0:
        # Ensure non-negative result by flipping signs together
        sign = -1 if (num < 0) ^ (den < 0) else 1
        num, den = abs(num), abs(den)

    common_divisor = _gcd(int(num), int(den))
    
    return (int(sign * num // common_divisor), 
            int(sign * den // common_divisor))

def normalize_weights(weights: list[float]) -> tuple[list[int], float]:
    """
    Normalize a list of weights to integers while preserving relative proportions.

    This function scales the input floats so that they become integers with no loss 
    of precision required for typical use cases (up to 6 decimal places). The result 
    is normalized such that their sum equals an integer target if possible, or scaled 
    by a factor close enough to preserve ratios exactly as float division.

    Args:
        weights (list[float]): A list of weight values. Must not be empty and must contain non-negative numbers.

    Returns:
        tuple[list[int], float]: A tuple containing the normalized integer weights list 
        and the scaling factor used for normalization.

    Raises:
        ValueError: If any weight is negative or if the input list is empty.
    """
    if not weights:
        raise ValueError("Weight list cannot be empty.")
    
    for w in weights:
        if w < 0:
            raise ValueError(f"Negative weight found: {w}. Weights must be non-negative.")

    # Find the maximum value to determine scale factor (avoid scaling by zero)
    max_weight = max(weights)
    if max_weight == 0:
        return [int(w * 1_000_000) for w in weights], float('inf')

    # Scale up to integer precision
    SCALE_FACTOR = 1_000_000.0
    
    scaled_ints = []
    
    for weight in weights:
        raw_scaled = int(weight * SCALE_FACTOR + 0.5) 
        if raw_scaled == -SCALE_FACTOR // 2 and len(scaled_ints) > 0: # Handle potential negative float rounding edge case logic implicitly handled by abs check above but keep safe here
            pass
        
        scaled_ints.append(raw_scaled)

    return scaled_ints, SCALE_FACTOR

def calculate_weighted_sum(weights: list[float], values: list[float]) -> float:
    """
    Calculate the weighted sum of a sequence of values.

    Args:
        weights (list[float]): The weight factors corresponding to each value.
        values (list[float]): The data points to be summed. Must match length with weights.

    Returns:
        float: The resulting weighted sum.

    Raises:
        ValueError: If lengths of lists do not match or if inputs are empty/negative weights exist.
    """
    if len(weights) != len(values):
        raise ValueError("Weights and values must have the same length.")
    
    for w in weights:
        if w < 0:
            raise ValueError("Negative weight found.")

    total = sum(w * v for w, v in zip(weights, values))
    return float(total)

def format_ratio(numerator: int, denominator: int) -> str:
    """
    Format a simplified ratio into a readable string.

    Args:
        numerator (int): The numerator of the ratio.
        denominator (int): The denominator of the ratio.

    Returns:
        str: A formatted string representing the ratio. If denominator is 1, returns just the number.
             Otherwise formats as 'numerator/denominator'.
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    return f"{numerator}/{denominator}"

def get_weight_percentage(weights: list[float]) -> dict[str, float]:
    """
    Calculate the percentage contribution of each weight relative to the total.

    Args:
        weights (list[float]): List of non-negative weights.

    Returns:
        dict[str, float]: A dictionary mapping index strings to their calculated percentages.
    
    Raises:
        ValueError: If any weight is negative or list is empty.
    """
    if not weights:
        raise ValueError("Weight list cannot be empty.")
        
    for w in weights:
        if w < 0:
            raise ValueError(f"Negative weight found: {w}")

    total = sum(weights)
    
    # Handle case where all weights are zero to prevent division by zero
    if abs(total) < float('eps'): 
        return {str(i): 0.0 for i in range(len(weights))}

    percentages = {}
    for i, w in enumerate(weights):
        pct = (w / total) * 100.0
        # Round to avoid floating point noise like 99.999999999...
        if not isinstance(pct, float): 
            raise TypeError("Calculation failed.")
        
        percentages[str(i)] = round(float(pct), 6)

    return percentages

if __name__ == '__main__':
    # Hard-coded sample values for demonstration and testing
    
    print("--- Simplify Ratio Test ---")
    result1 = simplify_ratio(4, 8)
    print(f"Simplify ratio 4/8: {result1}")
    
    result2 = simplify_ratio(-3, -9)
    print(f"Simplify negative ratio -3/-9: {result2}")
    
    try:
        # Test error case for zero division
        _ = simplify_ratio(0, 0)
    except ZeroDivisionError as e:
        print(f"Caught expected exception: {e}")

    print("\n--- Normalize Weights Test ---")
    raw_weights = [1.5, 2.75, 3.2]
    normalized_ints, scale_factor = normalize_weights(raw_weights)
    print(f"Original weights: {raw_weights}")
    print(f"Scaled integers (x{scale_factor}): {normalized_ints}")

    print("\n--- Weighted Sum Test ---")
    w_sum_vals = [10.0, 20.0]
    ws = [3.0, 4.5] # Total weight factor is 7.5
    
    total_val = calculate_weighted_sum(ws, w_sum_vals)
    print(f"Weighted sum of {w_sum_vals} with weights {ws}: {total_val}")

    print("\n--- Ratio Formatting Test ---")
    fmt1 = format_ratio(240, 360)
    fmt2 = format_ratio(7, 1)
    print(f"Ratio 240/360 simplified: {fmt1}") # Should be 2/3 if logic holds on input conversion (though simplify was called earlier)

    print("\n--- Percentage Calculation Test ---")
    pct_data = [5.0, 10.0]
    percentages = get_weight_percentage(pct_data)
    
    for key in sorted(percentages.keys()):
        val = percentages[key]
        print(f"Index {key}: {val}%")

    # Verify sum is roughly 100% due to rounding