def filter_even_numbers(numbers):
    """
    Filters a list of integers to return only even numbers.
    
    Args:
        numbers (list[int]): List of integers to process.
        
    Returns:
        list[int]: A new list containing only the even numbers from the input.
    """
    # Using list comprehension is generally optimized in Python for this task
    # compared to explicit loops or using filter() separately on large lists due to function call overhead.
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 3, 8, 5, 9, 2, 7, 6, 0]
    
    # Process the input list to filter even numbers
    result = filter_even_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered even numbers:", result)