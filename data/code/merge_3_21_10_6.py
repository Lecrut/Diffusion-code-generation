import sys

def sort_integers(data):
    """
    Sorts a list of integers in ascending order efficiently using Python's built-in Timsort.
    
    Args:
        data (list[int]): List of unsorted integers
        
    Returns:
        list[int]: Sorted list of integers
    """
    return sorted(data)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    sample_integers = [5, 2, 9, -1, 3, 8, 0, 7, 4]
    
    # Sort the list efficiently
    sorted_list = sort_integers(sample_integers)
    
    # Print the result to standard output as a single space-separated string per line or joined by spaces? 
    # The task says "prints the sorted list". Standard representation for lists in Python is [1, 2, ...]
    print(sorted_list)