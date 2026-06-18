import sys

def sort_integers(input_list):
    """
    Sorts a list of integers in ascending order using an efficient algorithm (Timsort).
    
    Parameters:
        input_list (list[int]): A list of unsorted integers.
        
    Returns:
        list[int]: The sorted list of integers.
    """
    return sorted(input_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    sample_data = [5, 2, 9, 1, 5, 6]

    # Perform sorting on the hard-coded data.
    sorted_data = sort_integers(sample_data)

    # Print the result to standard output as a space-separated list of integers.
    print(' '.join(map(str, sorted_data)))