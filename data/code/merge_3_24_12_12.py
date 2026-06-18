# Script to filter negative integers from a list using generator expression
# Reads input via standard stream (simulated with hard-coded values in main)
# Prints numbers that satisfy the condition: x < 0

def get_negative_numbers(numbers):
    """
    Generator function that yields only the negative numbers from the given iterable.
    
    Args:
        numbers (iterable of int): A sequence of integers to filter.
        
    Yields:
        int: Each integer in the input list if it is less than zero.
    """
    for num in numbers:
        # Check condition: number must be strictly negative
        if num < 0:
            yield num

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input or files are needed
    sample_data = [1, -5, 3.2, -9, 0, -4]

    # Use generator expression within list comprehension for filtering and printing
    negative_numbers_list = [num for num in get_negative_numbers(sample_data)]

    print("Negative numbers found:")
    for n in negative_numbers_list:
        print(n)