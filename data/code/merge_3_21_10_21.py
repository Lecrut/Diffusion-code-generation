def sort_integers(numbers):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    sorted_list = sort_integers(unsorted_list)

    # Print the result as a space-separated string to standard output for easy parsing if needed.
    print(" ".join(map(str, sorted_list)))