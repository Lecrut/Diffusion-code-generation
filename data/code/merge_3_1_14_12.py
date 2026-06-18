import numpy as np

def apply_percentage_change(weights: list[float], percent_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal fraction, e.g., 0.1 for +10%) 
    to every weight in the provided list.

    The operation is performed as: new_weight = old_weight * (1 + percent_change).

    Parameters:
        weights (list[float]): A list of numeric values representing initial measurements.
        percent_change (float): Decimal fraction indicating proportional change 
                               (e.g., 0.05 for a 5% increase, -0.20 for a 20% decrease).

    Returns:
        list[float]: New list containing updated weights after applying the percentage change.

    Optimization Note:
        While NumPy is used internally via @vectorize decorator to ensure high performance 
        on large datasets (up to millions of elements), the return type remains a native Python list
        for compatibility with existing code that expects lists over arrays. For extremely large data,
        users may directly utilize np.multiply(weights, 1 + percent_change) if they prefer array output.
    """
    
    @vectorize(native=False)
    def _apply_transform(weight):
        return weight * (1 + percent_change)

    # Convert input list to numpy array for optimized vectorized operation internally, then back to Python list on exit
    arr = np.asarray(weights, dtype=np.float64) if len(weights) > 0 else np.array([], dtype=np.float64)
    
    result_array = _apply_transform(arr)

    # Return as a standard Python list per requirements (unless array conversion was explicitly requested elsewhere in production logic)
    return [float(val) for val in result_array]

# Optional: Register vectorize function here since it's not part of stdlib. 
# Since the task requires "vectorized", we use np.vectorize which is standard but slow; 
# however, to truly optimize without external dependencies beyond NumPy, let's refactor slightly
# so that instead of using @np.vectorize (which isn't JIT'd), we perform direct numpy arithmetic internally and convert at end.

def apply_percentage_change_optimized(weights: list[float], percent_change: float) -> list[float]:
    """
    Optimized version applying percentage change to a weight list.
    
    Logic: 
        result = [w * (1 + pct) for w in weights] is slow due to Python loops on millions of items?
        Actually, pure Python loop with simple math can be surprisingly fast and avoids memory copies from array conversion if small lists used,
        but for 'highly optimized' per prompt: use numpy multiplication directly.

    Parameters are identical; output format adjusted accordingly."""
    
    # Ensure input is a list of numbers (float/int)
    weights = [w for w in weights] 
    percent_change = float(percent_change) 

    if len(weights) == 0:
        return []

    from numpy import array, multiply, ones
    
    arr_wts = array(weights, dtype='f8')  
    multiplier = 1.0 + percent_change 
    
    # Vectorized operation via NumPy multiplication (highly optimized C-level implementation handles large lists efficiently)
    new_arrs = multiply(arr_wts, multiplier)

    return [float(x) for x in new_arrs]

# Final function to be used — combining clarity and performance using pure numpy without unnecessary decorators 
def apply_percentage_change_final(weights: list[float], percent_change: float) -> list[float]:
    """Applies a specified percentage change (decimal) to every weight."""

    # Handle edge case of empty list immediately for speed
    if not weights:
        return []

    import numpy as np
    
    arr = np.array([float(x) for x in weights], dtype=np.float64)
    
    factor = 1.0 + float(percent_change)
    
    new_weights_arr = arr * factor
    
    # Convert back to native Python list of floats (required return format per task spec: "returning the new list")
    return [float(x) for x in np.array(new_weights_arr, dtype=np.float64)]

if __name__ == '__main__':
    sample_list = [10.5, 23.7, 89.2, -5.3, 0.0]
    percent_increase = 0.15  # Represents a 15% increase

    updated_weights = apply_percentage_change_final(sample_list, percent_increase)
    
    print("Original weights:", sample_list)
    print(f"Applying {percent_increase*100}% change")
    print("Updated weights:", updated_weights)