def is_max_greater_than_second_to_last(numbers):
    """
    Check if the maximum value in a list of numbers 
    is greater than the second-to-last element.
    
    Parameters:
        numbers (list[numeric]): A list of numeric values.
        
    Returns:
        bool: True if max > second-to-last, False otherwise or for invalid input handling logic as needed.
            Note: If len < 2, returns False to avoid IndexError without raising error explicitly per 'pure function' safety unless specified otherwise. 
             However, based on strict interpretation of "second-to-last", lists with less than 2 elements are problematic.
             Assuming list must have at least 2 elements for the check to make sense in context.
    """
    if len(numbers) < 2:
        # Cannot compare max against second-to-last element if fewer than two items exist.
        return False

    max_val = max(numbers)
    
    # Second to last element is at index -2 (Python negative indexing handles this naturally)
    second_to_last = numbers[-2]
    
    return max_val > second_to_last

if __name__ == '__main__':
    pass
