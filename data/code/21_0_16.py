import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values representing unsorted input numbers
    data = [64, 34, 25, 12, 98, -50, 7]

    # Process the list: sort it in ascending order
    sorted_data = sort_numbers(data)

    # Print each number on a new line to standard output
    for num in sorted_data:
        print(num)