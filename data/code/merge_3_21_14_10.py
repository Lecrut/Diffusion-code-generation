def sort_pairs(pairs):
    """
    Sorts a list of tuples based on the 'value' element in reverse order (descending).
    
    Each tuple in the input list is expected to be structured as (value, index), 
    where 'value' is used for sorting and 'index' serves as secondary metadata.
    
    Parameters:
        pairs (list[tuple]): A list of tuples containing at least two elements: 
                            a numeric value and an integer index.
                            
    Returns:
        list[tuple]: A new list with the same number of tuples, sorted in descending 
                    order by the 'value' element. The original list is not modified.

    Complexity Analysis:
        Time Complexity: O(n log n), where n is the length of the input list. This 
                        arises from sorting operations which dominate the function's runtime.
        
        Space Complexity: O(n) for storing the new sorted list, as a copy must be created 
                         to preserve the original order or if immutability is required.

    Example:
        >>> data = [(3, 0), (1, 2), (5, 4)]
        >>> sort_pairs(data)
        [(5, 4), (3, 0), (1, 2)]
        
    Raises:
        TypeError: If the input is not a list or if any element in the list is not a tuple.
    
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")
    
    for item in pairs:
        if not isinstance(item, tuple) or len(item) < 2:
            raise ValueError(f"Each element must be a tuple with at least two elements. Got {item}.")

    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [(15, 3), (7, 1), (24, 9), (15, 0)]
    
    sorted_result = sort_pairs(sample_data)
    
    print("Original data:", sample_data)
    print("Sorted data (descending by value):", sorted_result)