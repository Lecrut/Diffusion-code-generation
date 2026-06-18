"""
Weighted Average Ratio Calculator

This module provides a function to calculate the weighted average ratio 
from a list of weight ratios. The implementation uses standard library features,
ensures efficiency with O(n) time complexity, and includes comprehensive documentation.

The script accepts a list where each element is either:
1. A tuple/list representing [weight, value] pairs (e.g., [(w1, v1), (w2, v2)])
   OR 
2. Two separate lists of weights and values if passed as arguments to the function.

However, based on the task description "list of weight ratios", we interpret this 
as a list where each element is a pair [weight, value] or simply a single ratio 
if no explicit separation exists (though typically weighted average requires both).
To be robust and efficient: We will assume the input is a list of tuples/lists 
[weight_i, value_i].

If the user passes just one list containing raw ratios without weights, we treat them as equal weight.
But strictly following "list of weight ratios" usually implies pairs (Weight, Ratio).

Let's define the function signature to accept either:
- A single argument `data`: a list of [weight, value] tuples/lists.
OR for flexibility in testing scenarios without complex parsing logic being exposed 
to interactive prompts (which are forbidden), we will stick to one clear input format.

Input Format Assumption:
The script expects a list where each item is `[weight, ratio_value]`.
Example: [[10, 5], [20, 8]] -> Weighted average of ratios based on weights.

Calculation Logic:
Total Weight = sum(weights)
Weighted Sum = sum(weight * value for all pairs)
Average = Total Weighted Sum / Total Weight

Constraints Met:
- No input(), sys.stdin, argparse required args.
- Runs without user interaction or network access.
- Uses only standard library features (math is not strictly needed but good practice).
"""

def calculate_weighted_average(data):
    """
    Calculates the weighted average ratio from a list of weight-value pairs.

    Args:
        data (list[list[float]] | list[tuple]): A list where each element 
            represents [weight, value] or (weight, value). Weights and values must be numeric.
    
    Returns:
        float: The calculated weighted average ratio.
        
    Raises:
        ValueError: If the input is empty, contains non-numeric data, 
                   if weights are zero/negative causing division issues, 
                   or if pairs have mismatched lengths (though we assume consistent structure).
                   
    Complexity:
        Time: O(n) where n is the number of weight-value pairs.
        Space: O(1) auxiliary space excluding input storage.

    Example:
        >>> data = [[20, 5], [30, 8]] # Weights: 20, 30; Values/Ratios: 5, 8
        >>> calculate_weighted_average(data)
        7.4 (Calculation: ((20*5 + 30*8) / (20+30)) = (100+240)/50 = 340/50 = 6.8 -> Wait, let's recheck math in head.)
        Correction on example logic above for clarity: 
        Weighted Sum = 20*5 + 30*8 = 100 + 240 = 340
        Total Weight = 20 + 30 = 50
        Result = 340 / 50 = 6.8
        
    Note: 
        If the input list contains single numbers (ratios) without explicit weights,
        this function assumes equal weight for each ratio to avoid ambiguity in "list of ratios".
        However, per strict interpretation of "weight ratios", we expect pairs.
        To handle edge cases where a user might pass just one list of values assuming unit weights:
        We check if the first element is an int/float and not part of a pair structure? 
        Actually, to keep it simple and robust for the task description "list of weight ratios":
        If len(data) > 0 and isinstance(data[0], (int, float)) and all(isinstance(x, (int, float)) for x in data):
            # Treat as equal weights list
            w = [1.0] * len(data)
            v = data
        Else:
            # Assume pairs
            pass
        
    """
    
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list.")

    total_weight = 0.0
    weighted_sum = 0.0
    
    for item in data:
        # Handle case where input is just values (treat as equal weight=1)
        if isinstance(item, (int, float)) and not isinstance(item, tuple):
            w_val = 1.0
            v_val = item
        else:
            try:
                # Attempt to unpack as [weight, value] or (weight, value)
                parts = list(item)
                if len(parts) != 2:
                    raise ValueError(f"Each pair must have exactly two elements.")
                
                w_val = float(parts[0])
                v_val = float(parts[1])
            except (ValueError, TypeError):
                # Fallback or error handling for malformed input
                if isinstance(item, tuple) and len(item) == 2:
                    try:
                        w_val = float(item[0])
                        v_val = float(item[1])
                    except ValueError:
                        raise ValueError(f"Invalid pair format in data list.")
                else:
                    # If it's a single number but we didn't catch the int/float check above? 
                    # The initial check covers scalars. This block handles tuples/lists of length 2.
                    w_val = float(item[0]) if isinstance(item, (list, tuple)) and len(item) >= 1 else item
                    v_val = float(item[1]) if isinstance(item, (list, tuple)) and len(item) > 1 else item
                    
        # Validate weights are positive to avoid division by zero or negative weighting issues in this context
        if w_val <= 0:
            raise ValueError("Weights must be strictly greater than zero.")

        total_weight += w_val
        weighted_sum += (w_val * v_val)

    if total_weight == 0.0:
        return 0.0 # Or handle as undefined, but returning 0 is a safe default for empty weight sum
        
    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    
    # Sample Data: List of [weight, ratio] pairs
    # Pair 1: Weight=20, Ratio=5.0
    # Pair 2: Weight=30, Ratio=8.0
    sample_data = [[20, 5.0], [30, 8.0]]

    try:
        result = calculate_weighted_average(sample_data)
        
        print(f"Input Data: {sample_data}")
        print(f"Calculated Weighted Average Ratio: {result:.4f}")
        
        # Verification logic (optional internal check to ensure correctness in output description if needed, 
        # but the task asks for calculation only. We'll just print the result).
    except ValueError as e:
        print(f"Error during calculation: {e}")