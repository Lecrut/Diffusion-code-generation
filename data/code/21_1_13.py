def sort_by_descending(numbers):
    """
    Returns a new list containing integers from 'numbers' sorted in descending order.
    
    Args:
        numbers (list of int): The input list of integers to be sorted.
        
    Returns:
        list of int: A new list with elements sorted in descending order.
        
    Time Complexity: O(n log n) - Average and worst case for the sort algorithm used.
    Space Complexity: O(n) - For storing the result list (Python's Timsort is efficient).
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [5, 234, 1876, 90, 1]
    
    # Sort the sample data in descending order and display results
    result_list = sort_by_descending(sample_data)
    print("Original list:", sample_data)
    print("Sorted (descending):", result_list)

# Additional test cases if needed without user input
test_cases = [
    [],                      # Empty list
    [-10, -20, -30],        # Negative numbers only
    [42]                     # Single element
]

for i, tc in enumerate(test_cases, 1):
    print(f"\nTest case {i}:")
    output = sort_by_descending(tc)
    print("Input:", tc)
    print("Output:", output)