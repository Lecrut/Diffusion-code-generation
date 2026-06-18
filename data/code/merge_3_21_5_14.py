def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts the even numbers.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        tuple[list[int], int]: A tuple containing the sorted list and 
                               the count of even numbers found in the original list.
                               
    Time Complexity: O(n log n) due to sorting, where n is the number of elements.
    Space Complexity: O(n) for storing the copy during sorting if not using Timsort's optimization on partial data.
    """
    # Create a sorted copy of the input list
    sorted_numbers = sorted(numbers)
    
    # Count even numbers in the original list (or any order, as count is invariant to permutation)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_data = [5, 3, 8, 4, 9, 2, 7, 6]
    result_list, result_even_count = sort_and_count(sample_data)
    print(f"Sorted list: {result_list}")
    print(f"Count of even numbers: {result_even_count}")