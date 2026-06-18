def sort_by_descending(numbers):
    """
    Sorts a list of numbers in descending order using Python's built-in sorted function.
    
    Args:
        numbers (list): A list of numeric values to be sorted.
        
    Returns:
        list: A new list containing the elements from 'numbers' in descending order.
             The original list remains unchanged as per standard functional programming practices 
             unless specified otherwise, though Python's sort is often used for in-place mutation if preferred.
             Since the task asks to return a NEW list using built-ins optimally, sorted() is chosen over .sort().
    """
    # Using 'sorted()' returns a new list and sorts efficiently (Timsort algorithm)
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    sample_data = [3.14, 22, -5, 0, 789, 'apple', None] 
    try:
        sorted_result = sort_by_descending(sample_data)
        print("Sorted numbers (descending order):", sorted_result)
        
        # Additional numeric-only test case to ensure clarity if the user filters later
        numeric_only = [10, 5, -2, 3]
        result_numeric = sort_by_descending(numeric_only)
        print("Numeric list example:", result_numeric)
    except Exception as e:
        # Graceful handling in case of unexpected errors during execution
        print(f"An error occurred while sorting: {e}")