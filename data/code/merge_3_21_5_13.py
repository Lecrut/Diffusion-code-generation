def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts even numbers.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        tuple[list[int], int]: A tuple containing the sorted list 
                               and the count of even numbers from the original list.
       
    Time Complexity: O(n log n) due to sorting, where n is the number of elements in the input list.
                     Counting evens takes O(1) if done during sort or as a separate pass (O(n)).
"""
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Count even numbers from original unsorted list logic: 
    # Since we need to return stats based on "original" but sorting destroys original order,
    # however, parity is invariant under reordering. So counting evens after sort gives same result as before.
    even_count = sum(1 for num in sorted_numbers if num % 2 == 0)

    return (sorted_numbers, even_count)

if __name__ == '__main__':
    # Hard-coded sample values; no user input required
    sample_list = [34, 56, 78, 19, 23, 8, -12, 0]
    
    result_list, even_count = sort_and_count(sample_list)
    
    print("Sorted list:", result_list)
    print(f"Count of even numbers: {even_count}")