def is_even_recursive(n: int) -> bool:
    """
    Recursively determines if a non-negative integer is even.
    
    Base case: 0 is even.
    Recursive step: n-1 has the opposite parity of n, so we recurse until reaching base case.

    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if n is even, False otherwise.
    """
    if n == 0:
        return True
    # For positive integers, parity flips with each decrement
    else:
        return not is_even_recursive(n - 1)

def is_even_modulo(n: int) -> bool:
    """
    Directly determines if a non-negative integer is even using modulo operator.

    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if n is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments
    test_values = [0, 1, 2, 3, 4, 5, 100, 99]

    print("Testing recursive approach:")
    results_recursive = []
    for val in test_values:
        res = is_even_recursive(val)
        results_recursive.append(res)
    
    # Verify correctness against modulo method and count operations (simulated depth)
    max_depth = max(test_values) + 1
    
    print("Value | Recursive Result | Modulo Result | Correct?")
    for val in test_values:
        res_rec = is_even_recursive(val)
        res_mod = is_even_modulo(val)
        match = "Yes" if res_rec == res_mod else "No"
        # Estimate recursive calls roughly as n+1 due to base case inclusion logic above (0->T, 1->F(0), etc.)
        actual_calls_estimate = val + 1 
        print(f"{val:5} | {res_rec!s:<28} | {str(res_mod):<17} | {match}")

    # Efficiency Analysis Summary printed as part of the script execution output
    print("\nEfficiency Analysis:")
    print("- Recursive Approach:")
    print("  - Time Complexity: O(n) in terms of number of function calls.")
    print("  - Space Complexity: O(n) due to call stack depth (no tail-call optimization).")
    print("  - Critique: Highly inefficient for large n because it requires deep recursion, "
          "risking a 'RecursionError' on standard Python stacks. It performs unnecessary computations.")

    print("- Modulo Approach:")
    print("  - Time Complexity: O(1) constant time operations.")
    parity_check = is_even_modulo(test_values[-1])
    space_usage_estimate = "<stack frame>" if not isinstance(parity_check, int) else "O(1)" # Placeholder logic to show const space conceptually
    print("  - Space Complexity: O(1).")
    print("  - Critique: Optimal. Performs a single arithmetic operation regardless of input size.")

    # Final verification that both methods agree on all samples
    agreement = all(is_even_recursive(v) == is_even_modulo(v) for v in test_values)
    if agreement:
        print("\nConclusion: Both implementations produce correct results, but modulo is vastly more efficient.")
    else:
        print("\nERROR: Discrepancy found between recursive and modulo methods!")