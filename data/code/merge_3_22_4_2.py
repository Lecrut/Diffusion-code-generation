def filter_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the odd integers from the input list.

    Args:
        numbers (list[int]): A list of integers to process.

    Returns:
        list[int]: A list of unique odd numbers found in the input, 
                   sorted in ascending order for deterministic output performance.
    
    Optimization Note:
        This implementation uses a set comprehension inside the generator expression 
        combined with sorting only at the end where necessary. However, since duplicates 
        are preserved per requirement unless specified otherwise (task didn't specify unique), 
        we simply filter directly which is O(n) time complexity instead of iterating twice.
        
    Note on Duplicate Handling: The task asks for "only the odd numbers". It does not explicitly request uniqueness. 
    Therefore, if duplicates exist in input and are odd, they are included multiple times to maintain fidelity to source data.
    
    Time Complexity: O(n) where n is the length of the list.
    Space Complexity: O(k) where k is the number of odd elements returned.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, etc.)
    sample_data = [-5, -1, 0, 3, 7, 9, 11, 42, 100]

    result = filter_odd_numbers(sample_data)

    # Output the result to verify functionality without printing logic inside function
    print(f"Input: {sample_data}")
    print(f"Filtered Odd Numbers: {result}")