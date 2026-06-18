import sys

def sort_numbers(numbers):
    """Sorts a list of numbers in ascending order using Timsort."""
    return sorted(numbers)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, args, or files needed)
    sample_data = [64, 34, 25, 12, 98, 76]

    # Process the data: sort and print to standard output
    sorted_numbers = sort_numbers(sample_data)
    for num in sorted_numbers:
        sys.stdout.write(str(num) + '\n')