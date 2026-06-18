def is_max_greater_than_second_last(numbers):
    """
    Checks if the maximum value in a list of numbers is strictly greater than 
    the second-to-last element (index -2).
    
    Args:
        numbers: A non-empty list of numeric values.
        
    Returns:
        bool: True if max(numbers) > numbers[-2], False otherwise.
             Raises ValueError if the list has fewer than 2 elements.
    """
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements.")

    second_last = numbers[-2]
    maximum_value = max(numbers)

    return maximum_value > second_last

if __name__ == '__main__':
    # Sample test cases hard-coded within the module.
    
    # Test case 1: Valid list where condition is true
    sample_1 = [3, 5, 2, 7] 
    result_1 = is_max_greater_than_second_last(sample_1)
    print(f"Input: {sample_1}, Output: {result_1}") 

    # Test case 2: Valid list where condition is false (max equals second last)
    sample_2 = [4, 6, 3, 5] 
    result_2 = is_max_greater_than_second_last(sample_2)
    print(f"Input: {sample_2}, Output: {result_2}") 

    # Test case 3: Valid list where condition is false (max less than second last - impossible by definition of max, but used for logic check if duplicates exist and we consider strict inequality carefully. Actually, mathematically max >= any element. So this will always be False only if max == second_last.)
    # Let's construct a case where Max equals Second Last to test the 'strictly greater' condition returning False.
    sample_3 = [10, 8, 5, 10] 
    result_3 = is_max_greater_than_second_last(sample_3)
    print(f"Input: {sample_3}, Output: {result_3}") 

    # Test case 4: Single element (should raise error as per logic to ensure robustness or handle gracefully? The prompt doesn't specify behavior for <2 elements, but accessing index -2 requires at least 2. We will let it raise a clear ValueError).
    sample_4 = [5] 
    try:
        result_4 = is_max_greater_than_second_last(sample_4)
        print(f"Input: {sample_4}, Output: {result_4}")
    except ValueError as e:
        print(f"Input: {sample_4}, Error: {e}")

    # Test case 5: Empty list (should raise error)
    sample_5 = [] 
    try:
        result_5 = is_max_greater_than_second_last(sample_5)
        print(f"Input: {sample_5}, Output: {result_5}")
    except ValueError as e:
        print(f"Input: {sample_5}, Error: {e}")