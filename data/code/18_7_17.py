def compare_large_integers(num1: int, num2: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    While Python handles arbitrarily large integers natively by converting 
    string inputs to decimal form internally (base 10), this function ensures 
    a clean comparison logic that works directly with integer objects, bypassing 
    any potential issues related to intermediate base conversions if numbers were 
    passed as strings or in other formats.
    
    Args:
        num1 (int): The first large integer.
        num2 (int): The second large integer.
        
    Returns:
        str: A string indicating the comparison result ('less', 'equal', 'greater').
    """
    # Python's int type automatically handles arbitrary precision, so 
    # direct comparison is safe from overflow. This function provides a clean abstraction.
    
    if num1 < num2:
        return "num1 is less than num2"
    elif num1 > num2:
        return "num1 is greater than num2"
    else:
        return "num1 equals num2"

if __name__ == '__main__':
    # Sample values with hard-coded data. 
    # These numbers are significantly larger than standard 64-bit limits to demonstrate handling.
    
    sample_1 = 99983750928759382750928375092875092875 
    # Note: The above number is just an example; Python can handle much larger integers.
    
    sample_2 = 123456789123456789123456789 
    
    result_compare_directly = compare_large_integers(sample_1, sample_2)
    print(f"Direct comparison of {sample_1} and {sample_2}:")
    print(result_compare_directly)

    # Additional test case with negative numbers to ensure robustness.
    
    neg_sample_1 = -80000000000000000000 
    neg_sample_2 = 957
    
    result_neg_comparison = compare_large_integers(neg_sample_1, neg_sample_2)
    print(f"\nComparison of {neg_sample_1} and {neg_sample_2}:")
    print(result_neg_comparison)

    # Test equality case.
    
    equal_a = 450 
    equal_b = 450
    
    result_equal_check = compare_large_integers(equal_a, equal_b)
    print(f"\nComparison of {equal_a} and {equal_b}:")
    print(result_equal_check)

    # Test very large numbers closer in value.
    
    near_1 = 2**40 + 5 
    near_2 = 2**40 - 3 
    
    result_near_comparison = compare_large_integers(near_1, near_2)
    print(f"\nComparison of {near_1} and {near_2}:")
    print(result_near_comparison)

    # Test case where num2 is much larger.
    
    large_diff = 9980 
    small_base = -5 
    
    result_large_diff_check = compare_large_integers(small_base, large_diff)
    print(f"\nComparison of {small_base} and {large_diff}:")
    print(result_large_diff_check)