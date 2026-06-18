import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    unsorted_data = [64, 34, 25, 12, 98, 76]
    
    # Sort the data using the built-in sorted() function which uses Timsort (efficient for many datasets).
    sorted_numbers = sort_numbers(unsorted_data)
    
    # Print each number on a new line to standard output.
    print(sorted_numbers[0])
    if len(sorted_numbers) > 1:
        print(sorted_numbers[1])
        if len(sorted_numbers) > 2:
            print(sorted_numbers[2])