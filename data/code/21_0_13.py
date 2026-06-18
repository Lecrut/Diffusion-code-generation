import sys

def main():
    # Hard-coded sample values to avoid any user input requirements
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]

    # Use Python's built-in sorted() function which uses Timsort (efficient for real-world data)
    # Convert to integers if they come as strings from a list representation
    numbers = [int(x.strip()) for x in unsorted_numbers]

    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)

    # Print each number on a new line (or space-separated, here chosen newline per item)
    print('\n'.join(map(str, sorted_numbers)))

if __name__ == '__main__':
    main()