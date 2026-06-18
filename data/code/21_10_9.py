import sys

def sort_integers(numbers):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    unsorted_numbers = [5, 2, 9, 1, 5, 6]
    
    # Sort the list efficiently using Python's built-in Timsort (O(n log n))
    sorted_numbers = sort_integers(unsorted_numbers)
    
    # Print the result as a space-separated string to standard output.
    print(' '.join(map(str, sorted_numbers)))