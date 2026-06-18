import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Python's built-in Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    sample_data = [5, 2, 9, 1, 7, 3]

    if not isinstance(sample_data, list):
        raise TypeError("Input must be a list")

    sorted_result = sort_numbers(sample_data)

    # Print result to standard output, separated by spaces for clarity.
    print(' '.join(map(str, sorted_result)))