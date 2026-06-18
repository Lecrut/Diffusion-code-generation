import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access).
    raw_data = [54321, 98760, -12345, 0, 42]

    # Convert to integers and sort.
    sorted_list = sort_integers(raw_data)

    # Print the result as a space-separated string on standard output.
    print(" ".join(map(str, sorted_list)))