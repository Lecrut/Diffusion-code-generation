import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Python's built-in Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input or arguments needed)
    unsorted_list = [64, 34, 25, 12, 98, -10, 7]
    
    # Sort the list using the most efficient built-in method
    sorted_list = sort_numbers(unsorted_list)
    
    # Print the result to standard output (space-separated integers as is common convention for such tasks)
    print(' '.join(map(str, sorted_list)))