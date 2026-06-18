import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order using Timsort."""
    return sorted(int(x) for x in data)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or external dependencies needed.
    raw_input = "-5 3 -10 2 8 0 -3"

    parsed_data = [int(x) for x in raw_input.split()]
    sorted_list = sort_integers(parsed_data)
    
    print('\n'.join(map(str, sorted_list)))