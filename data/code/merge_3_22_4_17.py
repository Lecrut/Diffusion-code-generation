import sys

def filter_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to be filtered.
        
    Returns:
        list[int]: A list of odd integers found in the input.
    """
    # Generator expression is used for memory efficiency and concise logic.
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_data = [-5, 3, -10, 7, 0, 9, 4, 11]
    result = filter_odd_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Odd numbers:", result)