# Script to filter negative integers from a list using list comprehension
# No external input methods (input(), sys.stdin, etc.) are used; data is hard-coded in main block.

def get_negative_numbers(numbers):
    """
    Filters the given list of numbers and returns only those that are less than zero.
    
    Args:
        numbers (list[int]): A list containing integers to be filtered.
        
    Returns:
        list[int]: A new list containing only negative integers from the input list.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, args, or network access)
    sample_data = [-5, -10, 3, 7, -2, 0, 4, -8]

    print("Original list:", sample_data)

    negative_numbers = get_negative_numbers(sample_data)

    print("Negative numbers only:", negative_numbers)