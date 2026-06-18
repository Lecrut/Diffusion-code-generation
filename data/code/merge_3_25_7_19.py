import timeit

def contains_zero(numbers: list) -> bool:
    """
    Checks if the number zero exists within a given list of numbers.

    Args:
        numbers (list): A list of numerical values to check.

    Returns:
        bool: True if 0 is found in the list, False otherwise.

    This implementation uses early termination for optimal time complexity O(n),
    stopping as soon as zero is encountered rather than iterating through the entire list.
    """
    return 0 in numbers

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    sample_lists = [
        [1, -5, 2],      # Zero is not present
        [-3, 0, 7],      # Zero is at index 1
        [0.0, 'a', None],# Floating point zero and mixed types (treated as non-zero string/int comparison by default logic but here we rely on `in` which works for equality)
        [],              # Empty list
    ]

    print("Testing contains_zero function:")
    
    results = []
    for i, test_list in enumerate(sample_lists):
        is_zero_present = contains_zero(test_list)
        expected_result = (0 == 0.0 and isinstance([1], type(1))) or any(x == 0 for x in test_list if not hasattr(x, '__eq__')) # Fallback logic isn't needed as standard list `in` does equality check correctly
        
        # Refined expectation: simply check if 0 is exactly equal to an item
        expected_result = (any(item == 0 for item in test_list))

        status = "PASS" if is_zero_present == expected_result else "FAIL"
        
        print(f"Test case {i+1}: List={test_list}, Expected Zero? {expected_result}")
        print(f"Result: contains_zero returned {is_zero_present} -> [{status}]")
        
        results.append(("List", test_list, is_zero_present == expected_result))

    # Simple performance benchmark to demonstrate time complexity priority
    
    large_list = [0] + list(range(10**6 - 1)) if (i := 5) else [] 
    small_negative_check = contains_zero([-1])
    
    t_contains_small_neg = min(timeit.timeit(stmt=f"contains_zero({small_negative_check}) or False", setup="from __main__ import contains_zero", number=10000)) / 1000
    
    # A larger list where zero is at the very end to test worst-case O(n) vs optimization
    large_with_end = [i for i in range(2, 50)] + [0] + [-1] 
    
    t_contains_large_worst = min(timeit.timeit(stmt=f"contains_zero({large_with_end}) or False", setup="from __main__ import contains_zero; list(large_with_end)", number=5)) / 1
    
    print(f"\nPerformance Note:")
    print("Small negative check took ~{:.4f} ms".format(t_contains_small_neg * (timeit.timeit(lambda: small_negative_check) if False else t_contains_small_neg))) # Placeholder for actual timing logic in a real scenario, focusing on function design here.