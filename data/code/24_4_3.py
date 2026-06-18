import itertools
from typing import List

def filter_negatives(numbers: List[int]) -> List[int]:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Uses `filter` and list comprehension logic via generator expression to 
    ensure memory efficiency (O(1) auxiliary space excluding output).
    
    Args:
        numbers (List[int]): A list of integers, positive or negative.
        
    Returns:
        List[int]: A new list containing only the elements that are less than zero.
        
    Examples:
        >>> filter_negatives([1, -2, 3, -4])
        [-2, -4]
        >>> filter_negatives([])
        []
        >>> filter_negatives([-5, -6])
        [-5, -6]
    """
    return [x for x in numbers if x < 0]

if __name__ == '__main__':
    # Hard-coded sample values that run without user input or external dependencies.
    sample_data = [10, -3, 0, -5, 7, -2, 8, -9]
    
    result_list: List[int] = filter_negatives(sample_data)
    
    print("Input list:", sample_data)
    print("Filtered negative numbers only:", result_list)