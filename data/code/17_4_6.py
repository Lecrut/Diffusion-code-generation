def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimization note: Iterates through the list once, checking each element's parity.
    This is optimal for Python as it avoids unnecessary intermediate data structures 
    or complex filtering logic that would increase overhead.

    Args:
        numbers (list[int]): A list of integers to filter.

    Returns:
        list[int]: A new list containing only the even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = [1, 4, 6, 8, -2, 9, 10, 3.5, 12] 
    even_numbers = filter_even_numbers(sample_data)
    
    # Note: While the problem specifies integers in the type hint and description,
    # Python's modulo operator works with floats too (e.g., 3.5 % 2 != 0).
    # However, strictly adhering to "list of integers", we treat non-integers as odd/filtered out 
    # based on their mathematical remainder behavior in this context if passed incorrectly,
    # but the primary test data will be integers.

    print("Original list:", sample_data)
    print("Filtered even numbers:", even_numbers)