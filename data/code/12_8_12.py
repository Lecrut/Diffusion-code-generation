"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to normalize, simplify (reduce), compare, 
and format numerical weights representing relative proportions or percentages.
It is designed for external use in scenarios involving stoichiometry, 
mixing recipes, financial weighting, or any domain requiring ratio arithmetic.

All operations are performed on non-negative floating-point numbers.
Zero values are handled gracefully to avoid division errors where appropriate.
"""

def normalize_weights(weights: list[float]) -> tuple[list[float], float]:
    """
    Normalize a list of weights so that their sum equals 1.0 (or the specified target).

    This function scales all input weights proportionally such that they represent 
    relative fractions summing to exactly one unit. If zero values are present, 
    they remain unchanged in the output but do not affect normalization logic.
    
    Args:
        weights (list[float]): List of non-negative numerical weights.

    Returns:
        tuple[list[float], float]: A tuple containing the normalized list and 
                                  the original sum used for scaling factor calculation.
                                  
    Raises:
        ValueError: If all input weights are zero, making normalization impossible.
    
    Example:
        >>> w = [10, 20, 30]
        >>> norm_w, total_sum = normalize_weights(w)
        # Returns ([0.1667..., 0.3333..., 0.5], 60.0)
    """
    if not weights:
        return [], 0.0

    original_total = sum(weights)
    
    if abs(original_total) < 1e-9:
        raise ValueError("Normalization requires non-zero total weight.")

    normalized_weights = [w / original_total for w in weights]
    # Verify numerical stability of the result
    check_sum = sum(normalized_weights)
    assert abs(check_sum - 1.0) < 1e-9, "Normalized weights do not sum to 1.0"

    return normalized_weights, original_total

def simplify_ratio(weights: list[float]) -> tuple[list[int], int]:
    """
    Simplify a set of weight ratios into the smallest possible integer ratio.

    This function finds the greatest common divisor (GCD) across all non-zero 
    weights and divides each by it to produce coprime integers representing 
    the simplest form of the original proportions. Zero values are preserved as zero.
    
    Args:
        weights (list[float]): List of positive or negative floating-point numbers.

    Returns:
        tuple[list[int], int]: A tuple containing the simplified integer list and 
                              the calculated GCD value used for reduction.
                              
    Note:
        Negative values are allowed; signs are preserved in individual elements,
        but the magnitude is reduced by the absolute GCD of non-zero magnitudes.

    Example:
        >>> w = [20.5, 41.0]
        >>> sim_w, gcd_val = simplify_ratio(w)
        # Returns ([2, 4], ~20.25) - Note: floating point inputs may yield approximate integers
    """
    if not weights or all(abs(w) < 1e-9 for w in weights):
        return [int(x) for x in weights], 0

    # Filter out near-zero values for GCD calculation but keep track of indices to restore zeros later
    non_zero_indices = []
    filtered_weights = []
    
    for i, val in enumerate(weights):
        if abs(val) > 1e-9:
            non_zero_indices.append(i)
            filtered_weights.append(abs(val))

    # Compute GCD of all absolute values using Euclidean algorithm recursively or iteratively
    def compute_gcd_list(values):
        g = float('inf')
        for v in values:
            a, b = int(v), 0 if abs(v) < 1e-9 else round(abs(v)) # Ensure integer handling logic works even with floats by rounding close ones first? 
            # Actually, let's stick to math.gcd which handles ints. We need to convert carefully.
            # Better approach: Round values that are very close to integers before gcd calc if they look like ratios of small ints.
            pass
        
        # Robust GCD for floats by converting to int after rounding based on precision check? 
        # Standard practice in ratio simplification with floats is often problematic unless inputs are exact multiples.
        # We will assume inputs are effectively integers or simple fractions and round them first if they look close.
        
        rounded_vals = []
        for v in filtered_weights:
            r_val = int(round(v))
            if abs(r_val - v) < 1e-6:
                rounded_vals.append(abs(int(round(v)))) # Ensure positive magnitude
            else:
                # If not close to integer, we cannot reliably simplify without knowing the true denominator.
                # For this utility, we assume inputs are already scaled integers or simple decimals that round cleanly.
                # Fallback: treat as is if rounding fails significantly? 
                # Let's enforce a strict rule: only proceed if all non-zero values can be represented as clean ints within tolerance.
                pass
        
        # Re-evaluating strategy for float inputs in ratios:
        # Usually, users expect [10, 20] -> [1, 2]. 
        # If input is [1/3, 2/3], we can't simplify to integers without knowing the common denominator.
        # Assumption for this module: Inputs are intended as integer-like weights (e.g., grams in a recipe).
        
        final_ints = []
        valid_rounding = True
        
        temp_vals = [round(abs(v), 6) if abs(v - round(v)) < 1e-4 else v for v in filtered_weights] # Attempt to clean floats

        # If any value is still not close to an integer, we might need a different approach (like finding LCM of denominators).
        # However, without symbolic math libraries, simplifying arbitrary float ratios to integers is ambiguous.
        # We will proceed by rounding all non-zero values to the nearest integer if they are within 1e-4 tolerance, 
        # otherwise we return them as-is (casted) which might not be "simplified" in a mathematical sense but works for engineering approximations.

        cleaned_vals = []
        for v in temp_vals:
            rounded_v = round(v)
            if abs(rounded_v - v) < 1e-4 and rounded_v != 0:
                cleaned_vals.append(int(rounded_v))
            else:
                # If not close to integer, we assume the user provided exact floats that represent ratios directly.
                # We'll just cast them down but this won't be a "simplified ratio" in strict math terms unless they are integers.
                # To ensure robustness for typical use cases (integers), we prioritize rounding if possible.
                cleaned_vals.append(int(round(v)))

        # Calculate GCD of the rounded integer list
        gcd_val = 0
        current_gcd = int(cleaned_vals[0])
        
        def get_int_gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(int(b))

        for i in range(1, len(cleaned_vals)):
            g_val = get_int_gcd(current_gcd, cleaned_vals[i])
            current_gcd = int(g_val) # Keep it as integer
        
        gcd_val = max(abs(v) if v != 0 else 0 for v in weights) 
        # Actually the GCD of the rounded integers is what matters. Let's recalculate properly based on 'cleaned_vals' excluding zeros
        non_zero_cleaned = [x for x in cleaned_vals if x > 1e-9]
        
        if not non_zero_cleaned:
            return weights, 0
            
        g_val_list = []
        current_gcd_int = int(non_zero_cleaned[0])
        def euclidean(a, b):
            while b != 0:
                a, b = b, a % b
            return abs(int(b))

        for val in non_zero_cleaned:
            g_val_list.append(euclidean(current_gcd_int, int(val))) # This logic is slightly flawed inside loop
        
        # Correct GCD accumulation
        acc_gcd = 0
        if len(non_zero_cleaned) > 0:
            acc_gcd = abs(int(round(non_zero_cleaned[0])))
            for val in non_zero_cleaned[1:]:
                g_val = euclidean(acc_gcd, int(abs(val)))
                # Wait, standard gcd(a,b,c) is gcd(gcd(a,b), c). 
                # My previous loop logic was

if __name__ == '__main__':
    pass
