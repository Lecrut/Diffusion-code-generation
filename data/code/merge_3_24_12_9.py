"""
Script to filter negative integers from a list of numbers.
This module demonstrates filtering using a generator expression within print().
It does not use input(), sys.stdin, or any interactive prompts.
Instead, it uses hard-coded sample data in the main block for testing purposes.
"""

def get_negative_numbers(numbers):
    """
    Filters and yields only the negative numbers from the provided list of integers.

    Args:
        numbers (list[int]): A list containing integer values.

    Yields:
        int: The next negative number found in the input list, or None if none remain.
    
    Logic Explanation:
    - Iterates through each item in the `numbers` list.
    - Checks if an item is strictly less than zero (< 0).
    - If true, yields that integer; otherwise, skips it.
    """
    for num in numbers:
        if num < 0:
            yield num

def main():
    # Hard-coded sample values as per task requirements (no user input or files)
    sample_data = [3, -5, 10, -2, 0, -8, 7]

    print("Negative numbers in the list:")
    
    # Using a generator expression directly inside print() for memory efficiency and clarity
    result_generator = (num for num in sample_data if num < 0)
    print(list(result_generator))

if __name__ == '__main__':
    main()