def check_all_positive(numbers):
    """
    Checks if all numbers in the list are positive (greater than 0).
    
    Optimized by using a generator expression with early exit upon finding 
    any non-positive number, avoiding unnecessary iterations through the entire list.
    
    Args:
        numbers (list of int or float): The list to check.
        
    Returns:
        bool: True if all elements are positive, False otherwise.
    """
    return all(num > 0 for num in numbers)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [1, 2, 3],           # All positive -> True
        [-1, 2, 3],          # Contains negative -> False
        [],                  # Empty list (vacuously true for "all") -> True based on 'all' behavior
        [0.5, -0.5],         # One non-positive -> False
        [10, 20, 30]         # All positive integers -> True
    ]

    print("Testing check_all_positive function:")
    for i, test_list in enumerate(sample_lists):
        result = check_all_positive(test_list)
        print(f"List {i+1}: {test_list} => {result}")