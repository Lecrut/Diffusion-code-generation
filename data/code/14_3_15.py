import statistics as stats  # Only used if needed, but we'll implement manually for efficiency without imports unless necessary

def find_min_max_volumes(volume_list):
    """
    Returns a tuple (min_volume, max_volume) from the input list.
    
    This function is optimized to run in O(n) time complexity with minimal overhead.
    It avoids creating intermediate lists or sorting, which would be less efficient for large datasets.

    Args:
        volume_list (list): A list of numeric values representing volumes.

    Returns:
        tuple: A tuple containing the minimum and maximum values found in the list.
               If the list is empty, returns None for both elements or raises a ValueError if strictness is preferred.
    
    Raises:
        ValueError: If the input list is empty.
    """
    # Handle edge case immediately to avoid iteration on invalid data
    if not volume_list:
        raise ValueError("Input list cannot be empty.")

    min_val = float('inf')
    max_val = float('-inf')

    for value in volume_list:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return (min_val, max_val)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    sample_data = [100, 50, 200, 75, 30, 90]

    try:
        result_min, result_max = find_min_max_volumes(sample_data)
        
        # Output results directly to stdout for verification without interactive prompts
        print(f"Minimum Volume: {result_min}")
        print(f"Maximum Volume: {result_max}")
    except ValueError as e:
        print(f"Error: {e}")