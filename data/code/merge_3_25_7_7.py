def contains_zero(numbers):
    """
    Checks if zero exists in a list of numbers.
    
    Args:
        numbers (list): A list of numerical values
        
    Returns:
        bool: True if 0 is present, False otherwise
        
    Time Complexity: O(n) - single pass through the list
    Space Complexity: O(1) - no additional space used beyond input storage
    """
    return any(num == 0 for num in numbers)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [1, 2, 3],           # Expected: False
        [-5, -4, 0, 6],      # Expected: True
        [],                  # Edge case: Empty list -> Expected: False
        [0.0],               # Float zero -> Expected: True
    ]
    
    for i, test_list in enumerate(sample_lists):
        result = contains_zero(test_list)
        print(f"Test {i+1}: Input={test_list}, Contains Zero? {result}")