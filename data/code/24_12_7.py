"""
Script to filter negative integers from a list using a generator expression.
This module demonstrates reading data via standard input (simulated in main) 
and filtering values based on a condition without interactive prompts or arguments.
"""

def get_negative_numbers(numbers):
    """
    Generator function that yields only the numbers less than zero.

    Args:
        numbers (list[int]): A list of integers to be filtered.

    Yields:
        int: Each integer from the input list if it is negative.
    """
    for num in numbers:
        # Check condition: yield number only if strictly less than 0
        if num < 0:
            yield num

def main():
    # Hard-coded sample values as per requirements (no user input, args, or files)
    sample_data = [10, -5, 3.7, -2, 0, -9]

    # Use generator expression within list comprehension to collect results efficiently
    negative_numbers_list = [num for num in get_negative_numbers(sample_data)]

    # Print the filtered result with clear indication of what was processed
    print("Negative numbers found:", negative_numbers_list)

if __name__ == '__main__':
    main()