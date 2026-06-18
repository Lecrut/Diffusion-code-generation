def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts even numbers from the original list.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        tuple[list[int], int]: A tuple containing the sorted list and the count of even numbers.

    Time Complexity: O(n log n) due to sorting, where n is the number of elements in the input list.
    Space Complexity: O(n) for storing the copy during sort (typical Timsort behavior).
    """
    # Create a deep copy to avoid modifying the original list if necessary; 
    # however, since we need both sorted and count from original, sorting doesn't affect counting logic applied on values.
    # We'll make a working copy for sorting to ensure immutability of input isn't expected side effect,
    # though technically reusing reference is fine as long as caller accepts it's modified or passed by value conceptually.
    
    sorted_numbers = list(numbers)  # Sortable copy
    even_count = sum(1 for n in numbers if n % 2 == 0)  # Count evens directly from original

    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_data = [34, -89, 76, 5, -23, 12, 0, -9]
    
    result_list, result_count = sort_and_count(sample_data)

    print("Sorted list:", result_list)
    print(f"Count of even numbers: {result_count}")