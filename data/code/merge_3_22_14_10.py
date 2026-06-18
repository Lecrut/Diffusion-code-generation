def filter_odd_numbers(numbers):
    """
    Takes a list of integers and returns a new list containing 
    only the odd numbers from the input.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        list[int]: A list of odd integers found in the input.
        
    Complexity Analysis:
        Time: O(n), where n is the number of elements in the input list.
        Space: O(k), where k is the count of odd numbers (worst case O(n)).
    
    Examples:
        >>> filter_odd_numbers([1, 2, 3])
        [1, 3]
        >>> filter_odd_numbers([])
        []
        >>> filter_odd_numbers([-5, -4, 0, 6, 7])
        [-5, 7]
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Sample inputs (no user input required)
    sample_data = [10, 3, -4, 5, 0, 7, -2, 9, 6]

    result = filter_odd_numbers(sample_data)

    print("Input:", sample_data)
    print("Odd numbers only:", result)