import sys

def contains_zero(numbers: list) -> bool:
    """
    Checks if the number zero exists in the provided list of numbers.
    
    Args:
        numbers (list): A list containing numeric values.
        
    Returns:
        bool: True if 0 is found, False otherwise.
    """
    for num in numbers:
        if num == 0:
            return True
    return False

if __name__ == '__main__':
    # Sample data with various scenarios including zero and non-zero cases
    test_cases = [
        [1, 2, 3],           # No zero expected -> False
        [0, -5, 4],          # Zero at start -> True
        [-1, 0, 0.0],        # Multiple zeros including float representation of zero -> True (handled by equality)
        [],                  # Empty list -> False
    ]

    for test_case in test_cases:
        result = contains_zero(test_case)
        print(f"List: {test_case} | Contains Zero: {result}")