def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list with only the even integers from the input.
    """
    # Using list comprehension is more Pythonic and optimized than manual iteration in this context
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_input = [1, 4, 5, 8, 9, 6, -3, 0, 7]
    result_even = filter_even_numbers(sample_input)
    
    # Printing the result directly to console without user input
    print("Original list:", sample_input)
    print("Filtered even numbers:", result_even)