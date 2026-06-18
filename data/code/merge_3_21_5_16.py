def sort_and_count(numbers):
    """
    Accepts a list of numbers and returns:
        1. A sorted copy of the input list in ascending order.
        2. The total count of even numbers in the original (unsorted) list.
    
    Time Complexity: O(n log n) due to sorting, where n is the length of the list.
    Space Complexity: O(n) for creating a new sorted list and counting evens.
    """
    # Create a copy to avoid modifying the input if that were allowed/needed later
    numbers_copy = numbers[:]
    
    # Sort the copied list in ascending order using Timsort (Python's default, highly optimized)
    sorted_numbers = sorted(numbers_copy)
    
    # Count even numbers from the original unsorted list for accuracy regarding "original" count
    # Note: Sorting doesn't change parity counts, so counting on either is fine. 
    # We use the copy here to be explicit about processing order if logic were more complex later.
    even_count = sum(1 for num in numbers_copy if num % 2 == 0)
    
    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = [5, 3, 8, 1, 4, 9, 2, 7]
    
    result_sorted, result_even_count = sort_and_count(sample_data)
    
    print(f"Sorted List: {result_sorted}")
    print(f"Count of Even Numbers: {result_even_count}")