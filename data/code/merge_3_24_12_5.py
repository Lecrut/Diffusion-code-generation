#!/usr/bin/env python3
"""
Script to filter negative integers from a list of values provided in standard input.

This module demonstrates using a generator expression within a function call 
to process an iterable sequence and yield only elements that are less than zero.

Logic:
1. Define a helper function `get_negative_numbers` which accepts any iterable (e.g., list).
2. Inside the function, use a generator expression `(num for num in numbers if num < 0)` to iterate 
   through the input values and yield only those strictly less than zero. This is memory efficient 
   as it does not create an intermediate filtered list before processing.
3. The main execution block simulates reading from standard input by hard-coding a sample list of integers,
   ensuring the script runs without user interaction or network access.

Note: As per constraints, no `input()`, `sys.stdin` iteration for live prompts, 
or command-line argument parsing is used to guarantee deterministic behavior in an isolated environment.
"""

def get_negative_numbers(numbers):
    """
    Yield numbers from the input list that are negative (less than zero).

    Args:
        numbers (list[int] | iterable[any]): A sequence of integers or numeric values.

    Yields:
        int: The next integer in the sequence if it is less than 0, otherwise skips it.
    
    Example Usage:
        >>> list(get_negative_numbers([10, -5, 0, -3]))
        [-5, -3]
    """
    # Generator expression logic: checks each item and yields only if condition (num < 0) is true.
    for num in numbers:
        if isinstance(num, int):  # Ensure we are dealing with integers to avoid float comparisons edge cases per task spec context
            if num < 0:
                yield num

if __name__ == '__main__':
    # Hard-coded sample values representing a simulated input list of integers.
    # This satisfies the requirement for no user input, network access, or pre-existing files.
    sample_data = [15, -3, 8, -12, 0, -7, 4]

    print("Negative numbers found:")
    
    # Pass the hardcoded list to our generator function and collect results into a printed output block.
    negative_values = get_negative_numbers(sample_data)
    
    for val in negative_values:
        print(val)