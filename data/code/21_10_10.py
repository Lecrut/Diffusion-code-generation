import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, args, or network access).
    sample_data = [54321, 67890, -12345, 0, 1, 2, 3]

    sorted_result = sort_integers(sample_data)

    # Print the result as a space-separated string to standard output.
    print(" ".join(map(str, sorted_result)))