import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    raw_data = [5, 2, 9, 1, 7, 3]
    
    # Convert strings from JSON-like representation if necessary (simulating parsed input)
    integers = [int(x.strip()) for x in raw_data.split(',')]
    
    sorted_integers = sort_integers(integers)
    
    print(sorted_integers)