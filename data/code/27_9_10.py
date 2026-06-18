import sys

def compare_inequality(value1: float, value2: float) -> bool:
    """
    Compare two arbitrary numeric values to determine if they are strictly unequal.
    
    This implementation uses Python's native floating-point comparison which is 
    efficient and handles standard numerical edge cases appropriately for general use.
    
    Args:
        value1 (float): First numeric value.
        value2 (float): Second numeric value.
        
    Returns:
        bool: True if value1 != value2, False otherwise.
    """
    return value1 != value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        (3.0, 4.5),          # Standard integers/floating points - should be True
        (-17.896, -17.896), # Identical floats - should be False
        (float('inf'), float('-inf')), # Opposite infinities - should be True
        (0.0, 0.0),          # Zero equality - should be False
    ]

    for v1, v2 in samples:
        result = compare_inequality(v1, v2)
        print(f"compare({v1}, {v2}) -> {result}")