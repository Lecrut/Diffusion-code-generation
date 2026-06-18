def contains_zero(numbers):
    """
    Checks if zero exists within the provided list of numbers.
    
    This function iterates through the list exactly once, stopping immediately
    upon finding a zero to ensure optimal time complexity O(n).
    
    Args:
        numbers (list[bool]): A list containing numeric values where we check for 0
        
    Returns:
        bool: True if any element in the list is 0, otherwise False.

    Examples:
        >>> contains_zero([1, -2, 3])
        False
        >>> contains_zero([-1, 0, 5])
        True
    """
    
    for number in numbers:
        if number == 0:
            return True
            
    return False

if __name__ == '__main__':
    sample_list_1 = [42, -7, 13]
    sample_list_2 = [-5.0, 0, "text"]
    
    result_one = contains_zero(sample_list_1)
    print(f"List {sample_list_1}: Contains zero? {result_one}")
    
    result_two = contains_zero(sample_list_2)
    print(f"List {sample_list_2}: Contains zero? {result_two}")