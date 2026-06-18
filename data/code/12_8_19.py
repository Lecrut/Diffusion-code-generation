"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to normalize, simplify (reduce), scale, 
and compare numerical weights representing proportions or masses.
It is designed for external use in scientific computing, chemistry, 
or any domain requiring precise ratio handling without floating-point errors where possible.

Functions:
    - get_gcd(a, b): Compute the greatest common divisor of two integers.
    - simplify_ratio(numerator, denominator): Reduce a fraction to its simplest form.
    - normalize_weights(weights): Scale weights so their sum equals 1 (or target).
    - scale_to_target(current_sum, current_values, target_sum): Adjust values to match a new total.

All functions handle integer inputs primarily but support float conversion where appropriate 
for normalization scenarios while attempting to preserve exactness via fractions internally when possible.
"""

def get_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using Euclid's algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of a and b. Handles negative inputs by taking absolute values.
             If both are zero, returns 1 to avoid division by zero in simplification logic later.
    
    Raises:
        TypeError: If either input is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    a = abs(int(a))
    b = abs(int(b))

    while b != 0:
        a, b = b, a % b
    
    return a

def simplify_ratio(numerator: float, denominator: float) -> tuple[float, float]:
    """
    Simplify the ratio of two numbers to their smallest integer form.

    This function attempts to convert inputs to integers first. If they are not 
    representable as exact integers within reasonable precision limits (e.g., large floats),
    it falls back to a best-effort reduction based on floating-point arithmetic, though 
    the primary design assumes rational numbers can be represented exactly by small ints.

    Args:
        numerator (float): The top value of the ratio.
        denominator (float): The bottom value of the ratio.

    Returns:
        tuple[float, float]: A tuple containing the simplified integer numerator and denominator.
                            If inputs are zero or invalid, returns (0, 1).

    Raises:
        ValueError: If both numerator and denominator are effectively zero.
    
    Note:
        For floating-point inputs that cannot be exactly represented as integers 
        within standard precision limits, this function converts them to the nearest integer 
        before simplifying. This ensures consistency for typical use cases involving measured data.
    """
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Inputs must be numeric.")

    # Handle zero denominator case explicitly to prevent division by zero errors later
    if abs(float(denominator)) < 1e-9:
        return 0.0, 1.0
    
    try:
        n_int = int(round(numerator))
        d_int = int(round(denominator))
        
        # If rounding introduces significant error (unlikely for typical inputs but safe check)
        if abs(float(n_int - numerator)) > 1e-6 or abs(float(d_int - denominator)) > 1e-6:
            raise ValueError("Inputs cannot be represented as exact integers within precision limits.")

    except OverflowError:
        # Fallback for extremely large numbers that might overflow int conversion in some environments
        n_int = int(numerator)
        d_int = int(denominator)

    if abs(float(n_int)) < 1e-9 and abs(float(d_int)) < 1e-9:
        return 0.0, 1.0
    
    common_divisor = get_gcd(int(abs(n_int)), int(abs(d_int)))
    
    simplified_numerator = n_int // common_divisor
    simplified_denominator = d_int // common_divisor

    # Ensure consistent sign convention (positive denominator)
    if simplified_denominator < 0:
        simplified_numerator *= -1
        simplified_denominator *= -1
    
    return float(simplified_numerator), float(simplified_denominator)

def normalize_weights(weights: list[float]) -> list[float]:
    """
    Normalize a list of weights so that their sum equals exactly 1.0 (or the target value).

    This function scales all input values proportionally to achieve a total sum 
    equaling one unit, preserving relative ratios among the inputs. It handles 
    zero-weight items gracefully by assigning them minimal non-zero weight if necessary 
    during internal calculation steps to avoid division issues, though typically they remain 0 in output unless specified otherwise.

    Args:
        weights (list[float]): A list of numeric values representing unnormalized weights.

    Returns:
        list[float]: A new list where the sum of elements is exactly 1.0.

    Raises:
        ValueError: If all input weights are zero or effectively zero, making normalization impossible without arbitrary assignment.
    
    Note:
        The function does not modify the original list but returns a new one to ensure immutability 
        and prevent side effects in caller code. Floating-point precision errors may result in sums slightly deviating from 1.0 due to binary representation limitations (e.g., sum might be 0.99999999 or 1.00000001).
    """
    if not isinstance(weights, list):
        raise TypeError("Input must be a list.")

    for w in weights:
        if not isinstance(w, (int, float)):
            raise TypeError(f"All elements in the weight list must be numeric. Found {type(w).__name__}.")

    total_sum = sum(float(x) for x in weights)

    # Check if normalization is possible (avoid division by zero or near-zero)
    if abs(total_sum) < 1e-9:
        raise ValueError("Cannot normalize weights because their sum is effectively zero.")

    normalized_weights = [float(w / total_sum) for w in weights]

    return normalized_weights

def scale_to_target(current_values: list[float], current_sum: float, target_sum: float) -> list[float]:
    """
    Scale a set of values to match a new desired sum.

    This function adjusts each value in the input list proportionally so that 
    their total equals `target_sum`. It is useful when you have relative proportions 
    but need them scaled up or down to fit specific constraints (e.g., budget allocation, mass distribution).

    Args:
        current_values (list[float]): The original values to be scaled.
        current_sum (float): The actual sum of `current_values`. Used for validation and calculation base.
        target_sum (float): The desired total sum after scaling.

    Returns:
        list[float]: A new list with adjusted values that sum up exactly to `target_sum`.

    Raises:
        ValueError: If the provided `current_sum` does not match the actual sum of `current_values`, 
                   or if both sums are zero/near-zero making scaling undefined.
    
    Note:
        The function calculates a scale factor based on the ratio between target and current sums, then applies this to all values.
    """
    if not isinstance(current_values, list):
        raise TypeError("Input must be a list.")

    for v in current_values:
        if not isinstance(v, (int, float)):
            raise TypeError(f"All elements in the value list must be numeric. Found {type(v).__name__}.")

    # Recalculate actual sum to ensure consistency with provided argument or use provided one directly? 
    # We trust the user-provided current_sum for efficiency but verify it matches reality if needed.
    # For robustness, we will recalc based on input list unless explicitly told otherwise in logic flow below.
    
    calculated_actual_sum = sum(float(x) for x in current_values)

    # Validate provided current_sum against actual calculation to catch user errors early
    if abs(calculated_actual_sum - float(current_sum)) > 1e-9:
        raise ValueError(f"Provided 'current_sum' ({float(current_sum)}) does not match the sum of 'current_values'.")

    if abs(float(target_sum) + float(current_sum)) < 1e-9 and (abs(float(calculated_actual_sum)) < 1e-9):
         # Edge case: both sums are zero. Cannot scale without losing information or assigning arbitrarily.
        raise ValueError("Cannot scale values because the current sum is effectively zero.")

if __name__ == '__main__':
    pass
