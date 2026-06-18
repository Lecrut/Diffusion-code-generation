import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    raw_data = [5, 2, 9, 1, 5, 6]

    # Sort the data efficiently using Timsort (O(n log n)).
    sorted_list = sort_integers(raw_data)

    # Print the result as a space-separated string to standard output.
    print(' '.join(map(str, sorted_list)))