def compare_lengths(val_a: float, val_b: float) -> tuple[str, str]:
    """
    Compares two floating-point numbers to determine which is greater, less, or equal.
    
    Args:
        val_a (float): The first value to compare.
        val_b (float): The second value to compare.
        
    Returns:
        tuple[str, str]: A tuple containing the result strings ('a_greater', 'b_greater', 'equal').
                        The length string corresponds to which argument is larger in that context.
    
    Note: 
        This function uses direct comparison operators as requested for optimization clarity.
    """
    if val_a > val_b:
        return "a", "greater"
    elif val_b > val_a:
        return "b", "greater"
    else:
        # If neither is greater, they must be equal given float comparison stability in this context
        return "equal", None

if __name__ == '__main__':
    # Sample values to test the function without any user input or external dependencies.
    result_a = compare_lengths(5.0, 3.14)
    print(f"Comparison (5.0 vs 3.14): {result_a}")

    result_b = compare_lengths(2.718, 2.719)
    print(f"Comparison (2.718 vs 2.719): {result_b}")

    result_c = compare_lengths(0.5, float('inf')) # Testing edge case with infinity if supported by Python's comparison logic for floats in this scope or just standard floats
    
    # Focusing on direct floating point values as per task description
    result_equal = compare_lengths(42.0, 42.0)
    print(f"Comparison (42.0 vs 42.0): {result_equal}")

    # Additional explicit test for a greater case to ensure tuple structure consistency 
    result_d = compare_lengths(-10.5, -5.5)
    print(f"Comparison (-10.5 vs -5.5): {result_d}")