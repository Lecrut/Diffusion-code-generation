#!/usr/bin/env python3
"""
Module to filter negative integers from a list using list comprehension.
This script reads a predefined list of integers (hard-coded in main) 
and prints those that satisfy the condition x < 0.

Logic:
- Define a sample list containing positive, zero, and negative numbers.
- Use a list comprehension with an 'if' clause to filter only values less than zero.
- Print each filtered number on a new line separated by spaces (or newline if preferred).
"""

# Hard-coded sample data as per the requirement constraints
SAMPLE_LIST = [10, -5, 3, 0, -2, 7, -9]

def filter_negative_numbers(data_list):
    """
    Filters a list of integers to return only those that are negative.
    
    Args:
        data_list (list[int]): A list containing integer values.
        
    Returns:
        list[int]: A new list containing only the negative numbers from input.
    """
    # List comprehension syntax: [element for element in iterable if condition]
    # Here, we iterate through each number and keep it only if it is less than 0.
    return [number for number in data_list if number < 0]

def main():
    # Get the filtered list of negative numbers from our sample data
    negative_numbers = filter_negative_numbers(SAMPLE_LIST)
    
    # Print the result separated by spaces, as requested implicitly by "print" instruction context
    print(' '.join(map(str, negative_numbers)))

if __name__ == '__main__':
    main()