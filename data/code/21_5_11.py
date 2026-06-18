def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts the total number of even integers.
    
    Args:
        numbers (list[int]): A list of numerical values.
        
    Returns:
        tuple[list[int], int]: A tuple containing the sorted list and the count of even numbers.
    """
    # Create a copy to avoid modifying the original list if not intended, 
    # though typically sorting in-place is acceptable for functional requirements unless specified otherwise.
    # We'll sort directly on the input as it's often expected behavior unless immutability is required.
    sorted_numbers = sorted(numbers)
    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    
    return (sorted_numbers, even_count)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_data = [5, 3, 8, 4, 9, 12, 7, 10]

    result_list, result_even_count = sort_and_count(sample_data)

    print("Sorted list:", result_list)
    print(f"Count of even numbers: {result_even_count}")