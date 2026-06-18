import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    sample_data = [64, 34, 25, 12, 98, -10, 77, 43]

    # Sort the data in ascending order.
    sorted_list = sort_integers(sample_data)

    # Print each integer on a new line to standard output.
    for number in sorted_list:
        print(number)