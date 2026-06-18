def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts the even numbers.
    
    Args:
        numbers (list[int]): List of integers to process.
        
    Returns:
        tuple[list[int], int]: A tuple containing the sorted list and 
                              the count of even numbers from the original input.
    
    Time Complexity: O(n log n) due to sorting, where n is the length of the input list.
    Space Complexity: O(log n) for stack space used during sorting (Timsort), excluding output storage.
    """
    # Create a copy to avoid modifying the original input before counting evens from it directly if needed later
    sorted_numbers = sorted(numbers)
    
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
            
    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments)
    sample_list = [34, 78, 59, 62, 80, 1]
    
    result_sorted, result_even_count = sort_and_count(sample_list)
    
    print("Sorted list:", result_sorted)
    print("Count of even numbers:", result_even_count)