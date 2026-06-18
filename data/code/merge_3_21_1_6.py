def sort_by_descending(numbers: list) -> list:
    """
    Sorts a list of integers in descending order efficiently using Python's 
    built-in Timsort algorithm, which is optimized for real-world data.
    
    Args:
        numbers (list): A list of integers to be sorted.
        
    Returns:
        list: A new list containing the same integers sorted in descending order.
    """
    # Python's sorted() function uses Timsort, O(n log n), and is highly optimized.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    result = sort_by_descending(sample_data)
    
    # Output the result to verify functionality without external dependencies
    print(result)