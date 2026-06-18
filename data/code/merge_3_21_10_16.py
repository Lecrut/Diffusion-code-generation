import sys

def sort_integers(input_data):
    """
    Reads a list of integers from input data, sorts them in ascending order,
    and returns the sorted list efficiently using Timsort (Python's built-in).
    
    Args:
        input_data (list): A list of unsorted integers.
        
    Returns:
        list: The sorted list of integers.
    """
    return sorted(input_data)

if __name__ == '__main__':
    # Hard-coded sample values as per instructions to avoid user input or file dependencies
    sample_numbers = [5, 2, 9, 1, 5, 6]

    # Sort the list using an efficient algorithm (Timsort is O(n log n) worst-case average time complexity)
    sorted_list = sort_integers(sample_numbers.copy())
    
    # Print the result to standard output as a comma-separated string for clarity and robustness
    print(','.join(map(str, sorted_list)))