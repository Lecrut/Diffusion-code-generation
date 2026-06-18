import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files needed)
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    sorted_result = sort_integers(unsorted_list)

    # Print the result as a space-separated string to standard output
    print(" ".join(map(str, sorted_result)))