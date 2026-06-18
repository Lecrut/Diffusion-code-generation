def filter_negatives(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized by using a single pass loop instead of generator overhead 
    or map/filter which create intermediate objects in some Python versions/contexts,
    though for standard CPython [x for x in numbers if x < 0] is already highly optimized.
    This implementation uses explicit iteration to ensure clarity and minimal object creation.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: A new list containing only the negative elements from 'numbers'.
    
    Time Complexity: O(n) where n is the number of elements in the input list.
    Space Complexity: O(k) where k is the number of negative elements (for the output).
    """
    result = []
    for num in numbers:
        if num < 0:
            result.append(num)
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used.
    sample_data = [10, -3, 5, -7, 2, -89, 0, -4]

    filtered_result = filter_negatives(sample_data)

    print(f"Input: {sample_data}")
    print(f"Negative elements only: {filtered_result}")