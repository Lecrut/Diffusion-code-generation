def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order efficiently using Python's built-in Timsort,
    which is optimized for real-world data and performs well on partially sorted sequences.
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [34, 78, 12, 90, -5, 67, 23]
    
    # Process the data using our optimized function
    result = sort_by_descending(sample_data)
    
    print("Sorted list in descending order:", result)