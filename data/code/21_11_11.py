def sort_by_descending(numbers):
    """
    Sorts a list of numbers in descending order using Python's built-in optimized sorting.

    Args:
        numbers (list): A list of numeric values to be sorted.

    Returns:
        list: A new list containing the input numbers sorted from largest to smallest.
    """
    # The `sorted` function is highly optimized in CPython for performance.
    # It creates a new object and returns it, avoiding potential side effects on the original data structure.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_numbers = [5, 2, 9, -1, 7.5, 3]

    # Process the hard-coded sample values using our function
    result_sorted_list = sort_by_descending(sample_numbers)

    print(f"Original: {sample_numbers}")
    print("Sorted Descending:", result_sorted_list)