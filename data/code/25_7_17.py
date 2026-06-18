import time

def contains_zero(numbers):
    """
    Check if zero exists in a list of numbers.
    
    This function iterates through the list once to find the presence of zero,
    ensuring optimal O(n) time complexity where n is the length of the input list.
    Space complexity is O(1) as no additional data structures are used.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        bool: True if 0 is present in the list, False otherwise.
    """
    for num in numbers:
        if num == 0:
            return True
    return False

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files
    
    # Test case 1: Zero is present at the beginning
    list_a = [5, 7, 0, -3]
    
    # Test case 2: Zero is present in the middle/end
    list_b = [1.0, 'x', 0, False] 
    
    # Test case 3: No zero exists (integers)
    list_c = [-5, 10, -20]

    # Test case 4: Empty list
    list_d = []

    results = {
        "List A": contains_zero(list_a),
        "List B": contains_zero(list_b),
        "List C": contains_zero(list_c),
        "Empty List D": contains_zero(list_d)
    }

    print("Zero Detection Results:")
    for label, is_zero in results.items():
        if isinstance(is_zero, bool):
            status = f"Present!" if is_zero else "Not Present."
        else:
            # Fallback just in case logic fails unexpectedly though unlikely given type hints/usage
            status = str(is_zero) 
        print(f"{label}: {status}")

    # Optional performance check for non-empty list with zero present
    start_time = time.perf_counter()
    contains_zero(list_a)  # Triggers early exit
    end_time = time.perf_counter()
    
    if hasattr(time, 'perf_counter'):
        elapsed_ns = (end_time - start_time) * 1e9 
        print(f"\nExecution time for optimized search on sample data: {elapsed_ns:.6f} nanoseconds")