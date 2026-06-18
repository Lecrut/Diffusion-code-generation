import random

def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Timsort,
    which is highly optimized for real-world data including partially sorted sequences.
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the integers sorted in descending order.
    """
    # Timsort's default behavior is ascending; we reverse it after sorting or use a key with negation.
    # Negating values and then reversing avoids creating negative numbers if inputs are large,
    # but simply using sort(..., reverse=True) is the most direct and efficient in CPython for integers.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [34, 7, 23, 100, -5, 67, 98, 12]
    result = sort_by_descending(sample_data)
    print(result)