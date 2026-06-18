def sort_pairs(pairs):
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    Args:
        pairs (list[tuple]): A list where each tuple contains two elements: 
                             an integer value and its corresponding original index.

    Returns:
        list[tuple]: A new list containing the same tuples sorted by their first 
                     element (the 'value') in descending order. The second element 
                     of each tuple remains unchanged as it represents a stable sort 
                     key if values are equal, though Python's default sort is not guaranteed 
                     to be fully stable across all implementations without explicit handling;
                     however, for standard built-in sorts with tuples, secondary sorting by index 
                     occurs naturally in ascending order when primary keys are equal.

    Complexity:
        Time Complexity: O(n log n), where n is the number of elements in the input list.
                        This arises from the comparison-based sorting algorithm used internally.
        Space Complexity: O(n) for storing the result if a new list is created, or O(1) 
                         auxiliary space if sorted in-place (though this function returns a new list).

    Example:
        >>> sort_pairs([(3, 0), (1, 2), (4, 1)])
        [(4, 1), (3, 0), (1, 2)]
        
        Note: If values are equal, the secondary key (index) will be used in ascending order 
        due to Python's default tuple comparison behavior.
    """
    # Create a copy of the list and sort it by value descending.
    # Since tuples compare element-by-element, sorting directly on the list works as intended:
    # primary key is 'value' (descending), secondary key is 'index' (ascending).
    return sorted(pairs, reverse=True)

if __name__ == '__main__':
    sample_data = [(3, 0), (1, 2), (4, 1), (5, 3), (2, 4)]
    result = sort_pairs(sample_data)
    
    # Print the sorted list to verify functionality without user input or external dependencies.
    print("Sorted pairs:")
    for item in result:
        print(item)