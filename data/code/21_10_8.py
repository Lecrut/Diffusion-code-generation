import sys

def sort_integers(input_list):
    """Sorts a list of integers in ascending order using Timsort."""
    sorted_list = sorted(input_list)
    return sorted_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input is required
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    
    # Read the list (in this case using hard-coded data)
    integers_to_sort = sample_data
    
    # Sort and print the result
    sorted_integers = sort_integers(integers_to_sort)
    for number in sorted_integers:
        print(number)