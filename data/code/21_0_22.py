import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    unsorted_data = [64, 34, 25, 12, 98, 76, 54, 32]

    # Process the data: sort it in ascending order
    sorted_numbers = sort_numbers(unsorted_data)

    # Print the result to standard output (space-separated integers)
    print(" ".join(map(str, sorted_numbers)))