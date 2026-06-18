# Script to filter negative integers from a list using a generator expression.
# This module reads numbers directly from hardcoded sample data within its main block,
# avoiding any interactive input or external file dependencies.

def get_negative_numbers(numbers):
    """
    Generator function that yields only the negative numbers from the provided list.
    
    Args:
        numbers (list of int): A list containing integer values.
        
    Yields:
        int: Each number in the list if it is less than zero.
    """
    for num in numbers:
        # Check condition: yield only if the number is negative (< 0)
        if num < 0:
            yield num

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    sample_integers = [3, -5, 0, -2, 10, -8]
    
    # Use a generator expression to filter negative numbers efficiently
    filtered_negatives = get_negative_numbers(sample_integers)
    
    # Print the resulting negative numbers separated by spaces
    print(" ".join(map(str, filtered_negatives)))