import random

def filter_positive_numbers(numbers: list) -> list:
    """
    Processes a list of numbers and returns a new list containing only the positive elements.
    
    Args:
        numbers (list): A list of integers or floats to process.
        
    Returns:
        list: A list containing only the positive numbers from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample values without user interaction, network access, or file dependencies.
    test_data = [-5, 10, -3.5, 0, 42, -9, 7.8]
    
    result = filter_positive_numbers(test_data)
    
    print("Input:", test_data)
    print("Output (positive numbers only):", result)