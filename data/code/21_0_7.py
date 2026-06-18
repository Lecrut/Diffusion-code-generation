import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    sorted_result = sort_numbers(unsorted_list)

    print(sorted_result)