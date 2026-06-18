def sort_and_count(numbers):
    """
    Accepts a list of numbers and returns a tuple containing:
        1. The sorted list in ascending order.
        2. The total count of even numbers in the original list.
    
    Time Complexity: O(n log n) due to sorting, where n is the number of elements.
    Space Complexity: O(n) for storing the copy during sorting and counting.
    """
    # Create a sorted version of the input list (ascending order)
    sorted_numbers = sorted(numbers)
    
    # Count even numbers in the original list
    count_even = sum(1 for num in numbers if num % 2 == 0)
    
    return sorted_numbers, count_even

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_data = [5, 3, 8, 1, 4, 9, 2, 7]

    result_sorted, result_count = sort_and_count(sample_data)

    print("Sorted List:", result_sorted)
    print("Count of Even Numbers:", result_count)