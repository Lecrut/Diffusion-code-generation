def sort_and_count(numbers):
    """
    Returns a tuple containing:
        - A sorted list of numbers in ascending order (O(n log n))
        - The count of even numbers from the original input list
    
    Time Complexity Analysis:
        Sorting dominates at O(n log n). Counting evens is O(n) but done concurrently 
        with sorting or separately does not affect asymptotic complexity.
    
    Args:
        numbers (list): List of numerical values
        
    Returns:
        tuple: (sorted_list, even_count)
    """
    # Create a copy to preserve original list if needed for counting without mutation side effects
    sorted_numbers = sorted(numbers)  # O(n log n), stable sort
    
    # Count evens in the original list. Using enumerate or direct iteration is O(n).
    # Since we have 'sorted_numbers', we could count from there too, but to strictly 
    # reflect "original" behavior (though mathematically identical for counting property):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    
    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no input/output requirements are met.
    # Includes integers and floats where applicable (though integer logic applies here).
    sample_list = [34, -15, 78, 0, 9, 22, 6, -4, 1]

    result_tuple = sort_and_count(sample_list)
    
    sorted_data, even_quantity = result_tuple
    
    # Verification output (optional print for the single runnable module context)
    print(f"Sorted list: {sorted_data}")
    print(f"Total count of even numbers: {even_quantity}")