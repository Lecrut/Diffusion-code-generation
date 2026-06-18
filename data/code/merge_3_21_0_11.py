import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    unsorted_data = [64, 34, 25, 12, 98, -10, 77, 4]

    sorted_result = sort_numbers(unsorted_data)

    # Print each number on a new line as per standard output conventions for list processing.
    print('\n'.join(map(str, sorted_result)))