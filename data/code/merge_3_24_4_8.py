import sys

def filter_negative_numbers(numbers: list) -> list:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized by using list comprehension with early termination logic 
    where possible (though in pure iteration, order is fixed).
    Uses an explicit loop to avoid repeated list creation overheads during filtering.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing only the negative integers from 'numbers'.
    """
    
    result = []
    for num in numbers:
        if num < 0:
            result.append(num)
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access used.
    
    test_input = [34, -50, 78, -123, 96, -20]
    
    negative_numbers = filter_negative_numbers(test_input)
    
    print(f"Input: {test_input}")
    print(f"Negative numbers only: {negative_numbers}")