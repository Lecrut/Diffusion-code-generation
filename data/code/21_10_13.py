import sys

def sort_integers(numbers):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user input or file dependencies.
    unsorted_data = [5, 2, 9, 1, 7, 3]

    # Sort the data efficiently using Timsort (O(n log n)).
    sorted_data = sort_integers(unsorted_data)

    # Print each number on a new line to standard output.
    for num in sorted_data:
        print(num)