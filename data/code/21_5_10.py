def sort_and_count(numbers):
    """
    Sorts a list of numbers in ascending order and counts the even numbers from the original list.
    
    Args:
        numbers (list[int/float]): List of numeric values to process.
        
    Returns:
        tuple[list, int]: A tuple containing the sorted list and the count of even numbers.
       """
    # Create a copy to avoid modifying the input if necessary (though not strictly required by prompt)
    original = numbers[:]
    
    # Sort using Timsort which has O(n log n) average time complexity on typical data

if __name__ == '__main__':
    pass
