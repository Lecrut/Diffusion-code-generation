def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    Optimized using a generator expression within a list constructor to avoid 
    creating an intermediate list during iteration, improving both memory efficiency 
    and execution speed for large datasets.

    Args:
        numbers (list of int): The input list of integers.

    Returns:
        list of int: A new list containing only the even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network, or files)
    sample_data = [1, 4, 7, 8, 9, 16, 25, 32]

    result = filter_even_numbers(sample_data)

    print("Input:", sample_data)
    print("Filtered Even Numbers:", result)