def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        list[int]: A list containing only the odd numbers found in the input.
                   Returns an empty list if no odd numbers are present or 
                   if the input is not a list-like structure with iterables.
    
    Examples:
        >>> filter_odd_numbers([1, 2, 3])
        [1, 3]
        >>> filter_odd_numbers([])
        []
        >>> filter_odd_numbers([-5, -4, -3])
        [-5, -3]
        >>> filter_odd_numbers("not a list")
    """
    # Using a generator expression within list constructor for memory efficiency.
    return [n for n in numbers if isinstance(n, int) and not (n % 2 == 0)]

if __name__ == '__main__':
    sample_data = [10, 7, 34, 59, 8, -1]
    
    # Process the sample data to demonstrate functionality
    odd_numbers = filter_odd_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Odd numbers extracted:", odd_numbers)

# Note: The type hint `list[int]` assumes Python 3.9+. 
# For older versions, it would need to be `List[int]`, but given the requirement for a single runnable module, 
# modern syntax is preferred unless backward compatibility was explicitly requested beyond basic execution.