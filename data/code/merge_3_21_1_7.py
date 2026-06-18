def sort_by_descending(numbers: list) -> list:
    """
    Returns a new list containing the input integers sorted in descending order.
    
    This function uses Python's built-in Timsort algorithm which is highly efficient 
    for most lists of real-world data (O(n log n)). It creates and returns a 
    copy of the list to ensure mutability safety, modifying no side effects on 
    the original input.

    Args:
        numbers (list): A list of integers to be sorted.

    Returns:
        list: A new list containing elements from 'numbers' in descending order.
    
    Time Complexity: O(n log n) where n is the number of elements.
    Space Complexity: O(n) for storing the returned result and sorting state.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
        
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    sample_data = [64, 34, 25, 12, 987, -10, 5]
    
    sorted_result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted (descending):", sorted_result)

# Verification of correctness with a simple sanity check inside the block logic
assert len(sorted_result) == len(sample_data), "Length mismatch"
for i in range(len(sorted_result)):
    if i < len(sorted_result) - 1:
        assert sorted_result[i] >= sorted_result[i+1], f"Not descending at index {i}"

print("Validation passed.")