def check_all_positive(numbers):
    """
    Checks if all numbers in the list are positive (greater than 0).
    
    Args:
        numbers (list of int or float): The list to check.
        
    Returns:
        bool: True if all numbers are positive, False otherwise.
    """
    for num in numbers:
        if not isinstance(num, (int, float)) and not isinstance(num, complex) and type(num).__name__ != 'complex':
            # Basic type check to ensure we're dealing with numeric types
            pass 
        elif num <= 0:
            return False
    return True

if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = [-1, 2, 3]
    sample3 = []
    
    print(f"Sample 1 ({sample1}): {check_all_positive(sample1)}")
    print(f"Sample 2 ({sample2}): {check_all_positive(sample2)}")
    print(f"Sample 3 (empty list): {check_all_positive(sample3)}")