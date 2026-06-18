import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    sample_data = [64, 34, 25, 12, 98, -10, 72, 45]

    # Sort the data and print the result as a single line of space-separated integers.
    sorted_list = sort_integers(sample_data)
    
    # Output format: each integer on its own line for clarity in standard output streams.
    for number in sorted_list:
        print(number)