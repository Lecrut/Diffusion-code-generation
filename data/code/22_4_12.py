def extract_odds(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Optimized by using a generator expression within list comprehension,
    which avoids creating intermediate lists and is efficient in both time and space.
    
    Args:
        numbers (list of int): The input list of integers
        
    Returns:
        list of int: A new list containing only the odd numbers from the input
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]
    
    # Process the sample data to extract odd numbers
    result = extract_odds(sample_data)
    
    print(f"Input: {sample_data}")
    print(f"Odd numbers extracted: {result}")