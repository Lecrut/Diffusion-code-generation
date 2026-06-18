def contains_zero(numbers):
    """
    Checks if zero exists in a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        bool: True if 0 is present, False otherwise.
    """
    return any(num == 0 for num in numbers)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files
    sample_list_1 = [5, -3, 0, 7]
    sample_list_2 = [1, 2, 3, 4]
    sample_list_3 = []

    result_1 = contains_zero(sample_list_1)
    print(f"List {sample_list_1}: Zero exists? {result_1}")

    result_2 = contains_zero(sample_list_2)
    print(f"List {sample_list_2}: Zero exists? {result_2}")

    result_3 = contains_zero(sample_list_3)
    print(f"List {sample_list_3}: Zero exists? {result_3}")