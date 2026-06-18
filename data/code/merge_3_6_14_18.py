import statistics

def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A list containing numerical values representing weights.
        
    Returns:
        float: The difference between the max and min value, rounded to 6 decimal places 
               for floating-point precision consistency. Raises ValueError if input is empty.
        
    Complexity Analysis:
        Time: O(n) - Single pass through the list to find min and max.
        Space: O(1) - Constant extra space used regardless of input size (excluding input storage).
    
    Note: 
        While statistics.stdev() or similar functions exist, they are generally optimized for statistical calculations 
        but may have higher overhead than a simple manual comparison loop in Python due to function call and C-extension logic.
        For the specific task of finding min/max difference on large lists where only two values (min and max) need extraction,
        a direct approach avoids unnecessary intermediate data structures or complex algorithmic steps found in statistical libraries.
    """
    if not weights:
        raise ValueError("Input list cannot be empty.")

    # Using built-in functions is generally efficient as they are implemented in C for Python lists.
    # However, to ensure maximum efficiency and avoid any potential overhead of creating a new object 
    # (like the one from statistics module), we can use min() and max().
    # These are highly optimized but still involve function calls. For extremely tight performance constraints on massive data,
    # manual iteration in C-like loops would be faster, but pure Python's built-ins like min/max are standard for this task 
    # due to their optimization level compared to custom implementations without JIT compilers (like PyPy).
    
    return round(max(weights) - min(weights), 6)

if __name__ == '__main__':
    sample_weights = [10.5, 23.4, 89.7, 45.2, 12.1]
    result = calculate_weight_difference(sample_weights)
    print(f"Difference: {result}")