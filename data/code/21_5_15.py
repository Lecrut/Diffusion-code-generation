def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts even numbers from the original list.

    Args:
        numbers (list): A list of integers or floats representing numerical values.

    Returns:
        tuple: A tuple containing two elements:
            - The sorted version of the input list (ascending).
            - An integer count of even numbers in the original list.
    
    Time Complexity Analysis:
        Sorting takes O(n log n) due to Timsort used by Python's built-in sort().
        Counting evens is a linear pass at O(n).
        Overall time complexity: O(n log n), which is optimal for comparison-based sorting in this context.

    Example usage (see main block):
        input_list = [3, 8, 5, 2] -> returns ([2, 3, 5, 8], 2)
    """
    # Create a copy to avoid modifying the original list during processing if needed later
    sorted_numbers = sorted(numbers)

    even_count = sum(1 for num in numbers if isinstance(num, (int, float)) and num % 2 == 0)

    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_input = [3, -1, 4, 8, 5.5, 9, 2]
    
    result_list, result_even_count = sort_and_count(test_input)

    print(f"Sorted list: {result_list}")
    print(f"Count of even numbers: {result_even_count}")