def filter_odd_numbers(numbers):
    """
    Filters a list of integers to return only odd numbers.
    
    Optimized by using a generator expression which is memory efficient 
    compared to creating an intermediate filtered list, and avoids explicit loops.
    
    Args:
        numbers (list[int]): A list containing integer values.
        
    Returns:
        list[int]: A new list containing only the odd integers from the input.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network, or files)
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = filter_odd_numbers(sample_data)
    
    print(f"Input: {sample_data}")
    print(f"Filtered odd numbers: {result}")