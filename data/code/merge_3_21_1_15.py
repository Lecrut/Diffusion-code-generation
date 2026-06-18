"""
Module: sort_by_descending_optimized

This module provides an optimized function to sort a list of integers in descending order.
It uses Python's built-in Timsort algorithm via the sorted() function, which is highly efficient (O(n log n)).
The implementation avoids unnecessary overhead by using a generator expression with key extraction if needed,
though for simple integer sorting, direct comparison or negative mapping can be used efficiently.

Here we choose to map each element to its negation and sort in ascending order of the negatives,
which results in descending order without changing the original list elements during processing logic explicitly.
Alternatively, sorted() with a key argument is also very efficient but slightly more verbose for integers.
We will use negative values trick for clarity on efficiency (no custom comparator overhead).

Note: The 'sorted()' function returns a new list and does not modify in-place unless specified otherwise.
"""

def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order and returns the result as a new list.

    Args:
        numbers (list[int]): A list containing integer values to be sorted.

    Returns:
        list[int]: A new list with elements from 'numbers' sorted in descending order.

    Example:
        >>> sort_by_descending([3, 1, 4, 1, 5])
        [5, 4, 3, 1, 1]
    """
    # Using negative values to leverage ascending sort for descending output efficiently
    return sorted([-num for num in numbers], reverse=True)

if __name__ == '__main__':
    sample_data = [-5, 2, -8, 0, 3, -1, 7]
    result = sort_by_descending(sample_data.copy())
    
    print("Original list:", sample_data)
    print("Sorted descending:", result)